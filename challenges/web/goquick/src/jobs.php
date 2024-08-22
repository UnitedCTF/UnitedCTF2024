<?php
define("JOBS_FOLDER", "jobs/");
define("IP_REGEX", "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}");
define("URL_REGEX", "^https?:\/\/(" . IP_REGEX . "|[\w-]+(\.[\w-]+)*)(?::\d{1,5})?(?:\/.*|$)");

function register_job($old_id, $url) {
    if(isset($old_id)) {
        unlink(JOBS_FOLDER . $old_id . ".json");
    }

    $id = uniqid();
    $job = array(
        "id" => $id,
        "url" => $url,
        "state" => "waiting",
        "result" => "En attente de la prochaine mise à jour..."
    );

    $contents = json_encode($job);
    file_put_contents(JOBS_FOLDER . $id . ".json", $contents);

    return $id;
}

function get_job_result($id) {
    $contents = file_get_contents(JOBS_FOLDER . $id . ".json");
    $job = json_decode($contents, true);
    return $job;
}

function process_jobs() {
    $jobs = array_diff(scandir(JOBS_FOLDER), array(".", "..", ".htaccess"));

    foreach($jobs as $job_filename) {
        $contents = file_get_contents(JOBS_FOLDER . $job_filename);
        $job = json_decode($contents, true);
        if($job["state"] != "waiting") continue;

        $url = $job["url"];

        $matches = array();
        preg_match('@' . URL_REGEX . '@', $url, $matches);

        if(preg_match("/^" . IP_REGEX . "$/", $matches[1])) {
            if($matches[1] == "127.0.0.1") {
                $job["state"] = "error";
                $job["result"] = "Vous essayer d'accomplir quoi au juste? 🤨";
                goto save;
            }
        } else {
            $output = array();
            exec("dig +short A " . escapeshellarg($matches[1]), $output);
            if(count($output) == 0) {
                $job["state"] = "error";
                $job["result"] = "Le domaine que vous avez fourni n'existe pas... 😔";
                goto save;
            } else if($output[0] == "127.0.0.1") {
                $job["state"] = "error";
                $job["result"] = "Vous essayer d'accomplir quoi au juste? 🤨";
                goto save;
            }
        }

        $output = array();
        exec("curl -sS4gd @data/rides.json -m 5 --max-redirs 0 --proto =http,https " . escapeshellarg($url), $output);

        $output = join("\n", $output);
        if(strlen($output) > 256) $output = substr($output, 0, 256) . "...";

        if($output == "ok") {
            $job["state"] = "success";
            $job["result"] = "La mise à jour a été envoyée et reconnue.";
        } else {
            $job["state"] = "error";
            $job["result"] = "Une réponse invalide a été reçue de la part du serveur. La réponse attendue était \"ok\", la réponse reçue est \"" . $output . "\".";
        }

        save:
        $contents = json_encode($job);
        file_put_contents(JOBS_FOLDER . $job_filename, $contents);
    }
}
?>