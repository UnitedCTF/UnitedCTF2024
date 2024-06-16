<?php
if ($_SERVER["REQUEST_METHOD"] !== "POST") {
  header("Location: /");
  exit();
}

require_once("./partials/header.php");

echo "<pre>";
if (isset($_FILES["website"]) && isset($_FILES["website"]["tmp_name"]) && $_FILES["website"]["size"] < 5 * 1024 * 1024) {
  while (@ob_end_flush());
  $proc = popen("scripts/website-extractor.sh " . $_FILES["website"]["tmp_name"] . "; echo \"[*] Exit code $?\"", "r");
  $live_output = "";
  $full_output = "";
  while (!feof($proc)) {
    $live_output = fread($proc, 256);
    $full_output = $full_output . $live_output;
    echo htmlentities($live_output);
    @flush();
  }
  pclose($proc);

  preg_match('/[0-9]+$/', $full_output, $matches);
  $exit_code = intval($matches[0]);

  echo "\n\n";
  if ($exit_code === 0) {
    preg_match('/Extracting website to \'.*\/(.+?)\'/', $full_output, $matches);
    $subdomain = $matches[1];
    echo "[+] Deployment successful, redirecting ... (or <a href='/websites/" . $subdomain . "'>click here</a>)";
    echo "<script>setTimeout(() => window.location='/websites/" . $subdomain . "', 2500);</script>";
  } else {
    echo "[!] Deployment failed ...";
  }
} else {
  echo "[!] The website archive is either bigger than 1mb, missing or something really bad happened...";
  echo "\n\n\n[!] Deployment failed ...";
}
echo "</pre>";

require_once("./partials/footer.php");
