<?php

use Ratchet\WebSocket\WsServer;
use Ratchet\Http\HttpServer;

require __DIR__ . '/vendor/autoload.php';
require __DIR__ . '/src/WebSocketServer.php';

$db = new Database(__DIR__ . '/db/thrill-sync.db');
$ws = new WebSocketServer($db);

$wsServer = new WsServer($ws);

$server = Ratchet\Server\IoServer::factory(new HttpServer($wsServer), getenv("PORT"), '0.0.0.0');

$wsServer->enableKeepAlive($server->loop, 90);

$server->run();