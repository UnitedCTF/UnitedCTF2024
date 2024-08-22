<?php
require "jobs.php";

session_start();
header("Content-Type: " . "application/json");

if(isset($_SESSION["job"])) {
    $job = get_job_result($_SESSION["job"]);
    echo json_encode($job);
} else {
    echo "{}";
}
?>