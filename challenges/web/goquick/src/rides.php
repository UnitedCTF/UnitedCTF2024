<?php
define("RIDES_FILE", "data/rides.json");

function get_ride_times() {
    $contents = file_get_contents(RIDES_FILE);
    return json_decode($contents, true);
}

function update_ride_times() {
    $rides = get_ride_times();
    for($i = 0; $i < count($rides); ++$i) {
        $rides[$i]["waitTime"] = rand(0, 60);
    }
    $contents = json_encode($rides);
    file_put_contents(RIDES_FILE, $contents);
}
?>