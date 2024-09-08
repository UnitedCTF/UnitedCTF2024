<?php
if($_SERVER['REMOTE_ADDR'] != '127.0.0.1') {
    echo 'L\'accès à cette page est restreinte à l\'administrateur local!';
    die();
}

echo $_ENV['FLAG'];
?>