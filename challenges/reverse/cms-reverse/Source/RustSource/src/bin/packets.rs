use std::collections::HashMap;
use base64::Engine;
use base64::prelude::BASE64_STANDARD;
use crate::bin::hashing_util;
use crate::bin::http_handler::HTTP_Handler;
use crate::bin::packets::Packet::{F, OID, SanityCheck};

const SERVER_ID_HASH_KEY:&'static str = "SERVER_ID_HASH";
//1 byte for packet type, 32 bytes for server id
const MIN_PACKET_SIZE:u8 = 33;

pub struct OIDPacket{
    server_id:String,
    oid_request:u8
}

impl Identified<'_> for OIDPacket{
    fn get_id(&self) -> &String{
        &self.server_id
    }
}

impl OIDPacket{
    pub fn new(server_id:String,oid_request:u8) -> OIDPacket{
        OIDPacket{
            server_id,
            oid_request
        }
    }

    pub fn get_oid_request(&self) -> u8{
        self.oid_request
    }

    pub fn get_oid(&self) -> String{
        match self.oid_request {
            231 => "952809757913927".to_string(),
            122 => "204800000000000".to_string(),
            43 => "3670344486987776".to_string(),
            _ => "0".to_string()
        }
    }
}



pub struct FPacket{
    server_id:String,
    timestamp:u64,
    f_id:u64
}

impl Identified<'_> for FPacket{
    fn get_id(&self) -> &String{
        &self.server_id
    }
}

impl FPacket{
    pub fn new(server_id:String,timestamp:u64,f_id:u64) -> FPacket{
        FPacket{
            server_id,
            timestamp,
            f_id
        }
    }

    pub fn get_timestamp(&self) -> u64{
        self.timestamp
    }

    pub fn get_f_id(&self) -> u64{
        self.f_id
    }

    pub fn get_key(&self) -> String{
        let b64 = BASE64_STANDARD.encode(self.server_id.as_bytes());
        let mut bytes = Vec::new();
        for (i,byte) in b64.bytes().enumerate(){
            bytes.push(byte ^ self.timestamp.to_le_bytes()[i % 8]);
        }
        BASE64_STANDARD.encode(&bytes)
    }

}

impl<'a> Identified<'a> for SanityCheckPacket{
    fn get_id(&'a self) -> &'a String{
        &self.server_id
    }
}
pub struct SanityCheckPacket{
    server_id:String
}

impl SanityCheckPacket {
    pub fn new(server_id:String) -> SanityCheckPacket{
        SanityCheckPacket{
            server_id
        }
    }
}

trait Identified<'a>{
    fn get_id(&'a self) -> &'a String;
}

pub enum Packet{
    SanityCheck(SanityCheckPacket),
    F(FPacket),
    OID(OIDPacket),
}

impl Packet{
    fn get_identified_trait(&self) -> Option<&dyn Identified>{
        match self {
            SanityCheck(packet) => Some(packet),
            F(packet) => Some(packet),
            OID(packet) => Some(packet),
        }
    }

    pub fn from(mut raw:Vec<u8>) -> Result<Packet,&'static str>{
        if raw.len() < MIN_PACKET_SIZE as usize {
            return Err("Packet is too small")
        }
        let packet_type = raw.remove(0);
        match packet_type {
            0x0 => Ok(SanityCheck(SanityCheckPacket::new(String::from_utf8_lossy(raw.as_slice()).to_string()))),
            0x1 => {
                if raw.len() < (11 + MIN_PACKET_SIZE) as usize {
                    return Err("Packet is too small")
                }
                let timestamp_l = raw[0];
                raw.remove(0);
                let timestamp = String::from_utf8_lossy(raw.drain(0..timestamp_l as usize).as_slice()).to_string();
                let timestamp = match timestamp.as_str().parse(){
                    Ok(t) => t,
                    Err(_) => return Err("Invalid timestamp")
                };
                let sid = raw.drain(0..32).collect::<Vec<u8>>();

                let fid = String::from_utf8_lossy(raw.drain(0..10).as_slice()).to_string();
                let fid = match fid.as_str().parse(){
                    Ok(t) => t,
                    Err(_) => return Err("Invalid F ID")
                };
                Ok(F(FPacket::new(String::from_utf8_lossy(sid.as_slice()).to_string(),timestamp,fid)))

            },
            0xA => {
                if raw.len() < (MIN_PACKET_SIZE + 1) as usize {
                    return Err("Packet is too small")
                }
                let sid = String::from_utf8_lossy(raw.drain(0..32).as_slice()).to_string();
                Ok(OID(OIDPacket::new(sid,raw.remove(0))))
            },
            _ => Err("Unknown Packet type")
        }
    }

    fn get_id(&self) -> &String{
        &self.get_identified_trait().unwrap().get_id()
    }

    async fn init_hash(cache:&mut HashMap<String,String>,http_handler:&HTTP_Handler){
        match http_handler.do_get_request("74ba5d54-a5a7-4390-a1a1-4fdde2e66a05").await{
          Ok(response) => {
              cache.insert(SERVER_ID_HASH_KEY.to_string(),response);
          },
            Err(err) => panic!("{}",err)
        };
    }
    #[async_recursion::async_recursion]
    pub async fn validate_server_id(&self,cache:&mut HashMap<String,String>,http_handler: &HTTP_Handler) -> bool{
        match cache.get(SERVER_ID_HASH_KEY) {
            Some(hash) => hashing_util::compare_hash(self.get_id(), hash) ,
            None => {
                Packet::init_hash(cache,http_handler).await;
                self.validate_server_id(cache,http_handler).await
            }
        }
    }
}