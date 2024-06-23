<?php
session_start();
error_reporting(0);

if(isset($_GET['source'])) {
    highlight_file(__FILE__);
    die();
}
?>

<?php
require "rides.php";
require "jobs.php";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GoQuick</title>
    
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <main>
        <h1>Bienvenue au système GoQuick!</h1>
        <br>
        <h2>Voici les temps d'attentes courants:</h2>
        <p><em>Les temps d'attentes sont mis à jour aux 15 secondes...</em></p>
        <br>
        <table>
            <thead>
                <th>Nom du manège</th>
                <th>Temps d'attente</th>
            </thead>
            <tbody>
                <?php
                $rides = get_ride_times();
                foreach($rides as $ride) {
                    echo "<tr>\n";
                    echo "<td>" . $ride["name"] . "</td>\n";
                    echo "<td>" . $ride["waitTime"] . " minutes</td>\n";
                    echo "</tr>\n";
                }
                ?>
            </tbody>
        </table>
        <br>
        <h2>Vous voulez être le premier à recevoir la prochaine mise à jour?</h2>
        <p>Donnez-nous un URL et nous vous contacterons directement!</p>
        <br>
        <form method="POST">
            <input name="url" pattern="<?php echo URL_REGEX; ?>" placeholder="https://webhook.site/..."><button>Tenez-moi au courant!</button>
            <?php
            if(isset($_POST["url"])) {
                $url = $_POST["url"];
                if(!preg_match('@' . URL_REGEX . '@', $url)) {
                    echo "<br>Vous n'avez pas fourni un URL valide... 😢";
                } else {
                    echo "<br>Parfait! On vous envoie une mise à jour sous peu! 🙂";
                    $_SESSION["job"] = register_job($_SESSION["job"] ?? null, $url);
                }
            }
            ?>
        </form>
        <?php
        if(isset($_SESSION["job"])) {
            $job = get_job_result($_SESSION["job"]);
            echo "<br><p class=\"" . $job["state"] . "\">" . htmlspecialchars($job["result"], ENT_QUOTES, 'UTF-8') . "</p><br>";
        }
        ?>
        <br>
        <a href="/maintenance.php">Maintenance</a>
        <br>
        <a href="/assets/source.zip">Code source</a>
    </main>
</body>
</html>