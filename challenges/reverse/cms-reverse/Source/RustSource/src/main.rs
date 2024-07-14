#![feature(async_closure)]

use std::sync::LazyLock;

use crate::bin::tcp_handler::TCPHandler;

pub mod bin;
static TCP_HANDLER:LazyLock<TCPHandler> = LazyLock::new(|| TCPHandler::new());

#[tokio::main]
async fn main() {
    TCP_HANDLER.listen().await;
}
