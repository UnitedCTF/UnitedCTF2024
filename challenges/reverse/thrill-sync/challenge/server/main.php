<?php
use Ratchet\App;

require __DIR__ . '/vendor/autoload.php';
require __DIR__ . '/src/WebSocketServer.php';

$db = new Database(__DIR__ . '/db/thrill-sync.db');
$ws = new WebSocketServer($db);


$server = new App('0.0.0.0', getenv("PORT"));
$server->route('/websocket', $ws, ['*']);
$server->run();