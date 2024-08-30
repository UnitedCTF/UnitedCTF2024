<?php
use Ratchet\MessageComponentInterface;
use Ratchet\ConnectionInterface;

require_once __DIR__ . '/Database.php';

class WebSocketServer implements MessageComponentInterface
{
    protected $db;

    public function __construct(Database $db)
    {
        $this->db = $db;
    }

    public function onOpen(ConnectionInterface $conn)
    {
        $current_time = date('Y-m-d H:i:s');
        echo "[$current_time] New connection! ({$conn->resourceId})\n";
        $conn->send(json_encode(['action' => 'welcome', 'message' => 'Welcome to the ThrillSync WebSocket server']));
    }

    public function onMessage(ConnectionInterface $from, $msg)
    {
        $current_time = date('Y-m-d H:i:s');
        echo "[$current_time] Message received from {$from->resourceId}: $msg\n";
        $data = json_decode($msg, true);
        if (json_last_error() === JSON_ERROR_NONE) {
            if (isset($data['action'])) {
                switch ($data['action']) {
                    case 'attractions':
                        $from->send(json_encode(['action' => 'attractions', 'status' => 'success', 'attractions' => $this->db->getAttractions()]));
                        break;
                    case 'attraction':
                        if (isset($data['attraction'])) {
                            $from->send(json_encode(['action' => 'status', 'status' => 'success', 'attraction' => $this->db->getAttraction($data['attraction'])]));
                        } else {
                            $from->send(json_encode(['action' => 'status', 'status' => 'failure']));
                        }
                        break;
                    case 'flags':
                        if (isset($data['token'])) {
                            $flags = $this->db->getFlags($data['token']);
                            if (is_array($flags)) {
                                $from->send(json_encode(['action' => 'flags', 'status' => 'success', 'flags' => $flags]));
                            } else {
                                $from->send(json_encode(['action' => 'flags', 'status' => 'failure']));
                            }
                        } else {
                            $from->send(json_encode(['action' => 'flags', 'status' => 'failure', 'flags' => []]));
                        }
                        break;
                    case 'register':
                        if (isset($data['username']) && isset($data['password']) && isset($data["email"])) {
                            if ($this->db->register($data['username'], $data['password'], $data["email"])) {
                                $from->send(json_encode(['action' => 'register', 'status' => 'success']));
                            } else {
                                $from->send(json_encode(['action' => 'register', 'status' => 'failure']));
                            }
                        } else {
                            $from->send(json_encode(['action' => 'register', 'status' => 'failure']));
                        }
                        break;
                    case 'login':
                        sleep(2);
                        if (isset($data['username']) && isset($data['password'])) {
                            $token = $this->db->login($data['username'], $data['password']);
                            if ($token !== false) {
                                $from->send(json_encode(['action' => 'login', 'status' => 'success', 'token' => $token]));
                            } else {
                                $from->send(json_encode(['action' => 'login', 'status' => 'failure']));
                            }
                        } else {
                            $from->send(json_encode(['action' => 'login', 'status' => 'failure']));
                        }
                        break;
                    case 'logout':
                        if (isset($data['token'])) {
                            $this->db->logout($data['token']);
                            $from->send(json_encode(['action' => 'logout', 'status' => 'success']));
                            $from->close();
                        } else {
                            $from->send(json_encode(['action' => 'logout', 'status' => 'failure']));
                        }
                        break;
                    case 'ping':
                        $from->send(json_encode(['action' => 'ping', 'status' => 'pong']));
                        break;
                    default:
                        echo "[$current_time] Invalid action received from {$from->resourceId}: {$data['action']}\n";
                        $from->send(json_encode(['error' => 'Invalid action']));
                        break;
                }
            } else {
                echo "[$current_time] No action received from {$from->resourceId}\n";
                $from->send(json_encode(['error' => 'No action received']));
            }
        } else {
            $from->send(json_encode(['error' => 'Invalid JSON']));
            echo "[$current_time] Invalid JSON received from {$from->resourceId}: $msg\n";
        }
    }

    public function onClose(ConnectionInterface $conn)
    {
        $current_time = date('Y-m-d H:i:s');
        echo "[$current_time] Connection {$conn->resourceId} has disconnected\n";
    }

    public function onError(ConnectionInterface $conn, \Exception $e)
    {
        $current_time = date('Y-m-d H:i:s');
        echo "[$current_time] An error has occurred: {$e->getMessage()}\n";
        $conn->close();
    }
}