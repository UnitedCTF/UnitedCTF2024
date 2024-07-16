<?php
if(!file_exists("assets/source.zip")) {
    exec("zip source.zip *.php && mv source.zip assets/");
}
header("Location: " . "/assets/source.zip");
?>