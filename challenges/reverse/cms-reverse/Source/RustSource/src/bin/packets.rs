use std::collections::HashMap;
use base64::Engine;
use base64::prelude::BASE64_STANDARD;
use crate::bin::hashing_util;
use crate::bin::http_handler::do_get_request;
use crate::bin::packets::Packet::{CLN, F, SanityCheck};

const SERVER_ID_HASH_KEY:&'static str = "SERVER_ID_HASH";
//1 byte for packet type, 32 bytes for server id
const MIN_PACKET_SIZE:u8 = 33;
pub struct CLNPacket{
    server_id:String,
    timestamp:u64,
    cln: String
}
impl Identified<'_> for CLNPacket{
    fn get_id(&self) -> &String{
        &self.server_id
    }
}

impl CLNPacket{
    pub fn new(server_id:String,timestamp:u64,cln:String) -> CLNPacket{
        CLNPacket{
            server_id,
            timestamp,
            cln
        }
    }

    pub fn get_timestamp(&self) -> u64{
        self.timestamp
    }

    pub fn get_cln(&self) -> &String{
        &self.cln
    }

    pub fn get_key(&self) -> String{
        let b64 = BASE64_STANDARD.encode(format!("{}@{}",self.server_id,self.cln).as_bytes());
        let mut bytes = Vec::new();
        for (i,byte) in b64.bytes().enumerate(){
            bytes.push(byte ^ self.timestamp.to_le_bytes()[i % 8]);
        }
        let b64 = BASE64_STANDARD.encode(&bytes);
        let mut bytes2 = Vec::new();
        let sid_chars = self.server_id.bytes().collect::<Vec<u8>>();
        for (i,byte) in b64.bytes().enumerate(){
            bytes2.push(byte ^ sid_chars[i % sid_chars.len()]);
        }
        BASE64_STANDARD.encode(&bytes2)
    }
}
pub struct FPacket{
    server_id:String,
    timestamp:u64,
    f_id:u32
}

impl Identified<'_> for FPacket{
    fn get_id(&self) -> &String{
        &self.server_id
    }
}

impl FPacket{
    pub fn new(server_id:String,timestamp:u64,f_id:u32) -> FPacket{
        FPacket{
            server_id,
            timestamp,
            f_id
        }
    }

    pub fn get_timestamp(&self) -> u64{
        self.timestamp
    }

    pub fn get_f_id(&self) -> u32{
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
    CLN(CLNPacket)
}

impl Packet{
    fn get_identified_trait(&self) -> Option<&dyn Identified>{
        match self {
            SanityCheck(packet) => Some(packet),
            F(packet) => Some(packet),
            CLN(packet) => Some(packet)
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
                let timestamp = u64::from_be_bytes([raw[0],raw[1],raw[2],raw[3],raw[4],raw[5],raw[6],raw[7]]);
                raw.drain(0..8);
                let sid = &raw[0..32];
                Ok(F(FPacket::new(String::from_utf8_lossy(sid).to_string(),timestamp,u32::from_be_bytes([raw[32],raw[33],raw[34],raw[35]]))))
            },
            0xC => {
                if raw.len() < (8 + MIN_PACKET_SIZE) as usize {
                    return Err("Packet is too small")
                }
                let timestamp = u64::from_be_bytes([raw[0],raw[1],raw[2],raw[3],raw[4],raw[5],raw[6],raw[7]]);
                raw.drain(0..8);
                let sid = String::from_utf8_lossy(raw.drain(0..32).as_slice()).to_string();
                Ok(CLN(CLNPacket::new(sid,timestamp,String::from_utf8_lossy(raw.as_slice()).to_string())))
            },
            _ => Err("Unknown Packet type")
        }
    }

    fn get_id(&self) -> &String{
        &self.get_identified_trait().unwrap().get_id()
    }

    async fn init_hash(cache:&mut HashMap<String,String>){
        println!("Init hash");
        match do_get_request("74ba5d54-a5a7-4390-a1a1-4fdde2e66a05").await{
          Ok(response) => {
              println!("Server id hash: {}",response);
              cache.insert(SERVER_ID_HASH_KEY.to_string(),response);
          },
            Err(err) => panic!("{}",err)
        };
    }
    #[async_recursion::async_recursion]
    pub async fn validate_server_id(&self,cache:&mut HashMap<String,String>) -> bool{
        match cache.get(SERVER_ID_HASH_KEY) {
            Some(hash) => hashing_util::compare_hash(self.get_id(), hash) ,
            None => {
                Packet::init_hash(cache).await;
                self.validate_server_id(cache).await
            }
        }
    }
}