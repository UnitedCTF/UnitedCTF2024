use std::collections::HashMap;

use const_format::formatcp;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::{TcpListener, TcpStream};
use tokio::sync::Mutex;
use crate::bin::http_handler::{do_get_request, do_post_request};
use crate::bin::packets::{ FPacket, Packet};

const PORT:u32 = 11954;
const URL:&'static str = formatcp!("127.0.0.1:{}",PORT);
const FLAG:&'static str = "flag-H3yD0ntL0okH3re";

pub struct TCPHandler{
    cache:Mutex<Box<HashMap<String,String>>>
}
impl TCPHandler{
    pub fn new() -> TCPHandler{
        if FLAG.len() != 20{
            panic!("huh??");
        }
        TCPHandler{
            cache:Mutex::new(Box::new(HashMap::new()))
        }
    }
    pub async fn listen(&'static self){
        let listener = TcpListener::bind(URL).await.unwrap();
        loop{
            let (stream,_) = listener.accept().await.unwrap();
            tokio::spawn(async {
                self.handle_connection(stream).await;
            }).await.unwrap();
        }

    }
    async fn handle_connection(&self, mut stream: TcpStream) {
        let mut buffer = [0; 1024];
        loop {
            let n = match stream.read(&mut buffer).await {
                Ok(n) if n == 0 => return,
                Ok(n) => n,
                Err(e) => {
                    eprintln!("failed to read from socket; err = {:?}", e);
                    return;
                }
            };
            let received = &buffer[..n];
            let s = match Packet::from(received.to_vec()){
                Ok(packet) => {
                    self.handle_packet(&packet).await
                },
                Err(err) => {
                    format!("Failed to parse packet; err = {:?}",err).into_bytes()
                }
            };
            if let Err(e) = stream.write_all(s.as_slice()).await {
                eprintln!("failed to write to socket; err = {:?}", e);
                return;
            };

        }
    }

    async fn handle_packet(&self,packet:&Packet) -> Vec<u8>{
        if !packet.validate_server_id(self.cache.lock().await.as_mut()).await{
            return "Invalid Server ID".to_string().into_bytes()
        }
        match packet {
            Packet::SanityCheck(_) => self.handle_sanity_check_packet().await,
            Packet::F(packet) => self.handle_f_packet(packet).await,
            Packet::OID(packet) => packet.get_oid().to_string().into_bytes()
        }
    }

    async fn handle_sanity_check_packet(&self) -> Vec<u8>{
            do_get_request("a5276b40-5acf-44a8-b0d0-56819516145f").await.unwrap().into_bytes()
    }
    async fn handle_f_packet(&self,packet:&FPacket) -> Vec<u8>{
        match packet.get_f_id() {
            2341463483 => do_post_request("61209e4d-3da2-42e8-a2aa-e1d5f281854b",vec![("timestamp".to_string(),packet.get_timestamp().to_string()),("key".to_string(),packet.get_key())].as_slice()).await.unwrap().into_bytes(),
            3708838548 => do_post_request("9f18010c-c4e9-47a9-8545-ffda55cd03cc",vec![("timestamp".to_string(),packet.get_timestamp().to_string()),("key".to_string(),packet.get_key())].as_slice()).await.unwrap().into_bytes(),
            _ => "Unknown F ID".to_string().into_bytes()
        }
    }
}


