#![feature(async_closure)]

use std::borrow::ToOwned;
use std::clone::Clone;
use std::env;
use std::process::exit;
use std::string::ToString;
use std::sync::LazyLock;
use crate::bin::tcp_handler::TCPHandler;
use crate::bin::http_handler::HTTP_Handler;
pub mod bin;
static  TCP_HANDLER:LazyLock<TCPHandler> = LazyLock::new(|| TCPHandler::new(env::args().collect::<Vec<String>>().get(1).unwrap().to_string(),env::args().collect::<Vec<String>>().get(2).unwrap().to_string()));

#[tokio::main]
async fn main() {
    let arg_length = env::args().collect::<Vec<_>>().len();
    if arg_length < 3 {
        println!("Not enough arguments: expected 2, got {}. usage: CMS-PRO_BACKEND [SERVER_ADDR] [SERVER_PORT]", arg_length - 1);
        exit(1)
    }
    TCP_HANDLER.listen().await;
}
