# GoQuick

## Write-up

En visitant le challenge, on peut voir qu'il y a une page `/maintenance.php`. Malheureusement on ne peut pas la consulter.<br>
En regardant dans le code, on peut voir que l'addresse IP de source doit être `127.0.0.1`, soit l'IP loopback du serveur.

```php
<?php
if($_SERVER['REMOTE_ADDR'] != '127.0.0.1') {
    echo 'L\'accès à cette page est restreinte à l\'administrateur local!';
    die();
}

echo $_ENV['FLAG']; // 👀
?>
```

*Heureusement* pour nous, le site offre une fonctionnalité de notifications via webhook qui nous permet de faire des requêtes en tant que le serveur (un beau SSRF), ça pourrait nous permettre de satisfaire la condition pour visiter `/maintenance.php`.

Cependant, en essayant des URLs tels que `http://127.0.0.1/maintenance.php` ou encore `http://localhost/`, on obtient une erreur obscure:

> Vous essayer d'accomplir quoi au juste? 🤨

Si on regarde dans le code (dans le fichier `jobs.php`), on peut voir qu'il y a une validation pour vérifier qu'on n'envoie pas un URL avec l'IP `127.0.0.1`. Similairement, si on envoie un nom de domaine, une requête DNS est envoyée (avec `dig`) pour vérifier que ce domaine ne résout pas à `127.0.0.1`.

```php
if(preg_match("/^" . IP_REGEX . "$/", $matches[1])) {
    if($matches[1] == "127.0.0.1") {
        $job["state"] = "error";
        $job["result"] = "Vous essayer d'accomplir quoi au juste? 🤨";
        goto save;
    }
} else {
    $output = array();
    // première requête DNS ici
    exec("dig +short A " . escapeshellarg($matches[1]), $output);
    if(count($output) == 0) {
        // ...
    } else if($output[0] == "127.0.0.1") {
        $job["state"] = "error";
        $job["result"] = "Vous essayer d'accomplir quoi au juste? 🤨";
        goto save;
    }
}

$output = array();
// deuxième requête DNS ici
exec("curl -sS4gd @data/rides.json -m 1 --max-redirs 0 --proto =http,https " . escapeshellarg($url), $output);
```

Puisque deux requêtes DNS sont faites, soit une avec `dig` et une au moment de la requête avec `curl`, on peut contourner la restriction avec du round-robin DNS.

En effet, on peut créer un nom de domaine avec deux entrées `A`, une qui pointe vers un IP aléatoire comme `1.1.1.1` et une qui pointe vers `127.0.0.1`. Avec le round-robin (offert par la plupart des registraires/serveurs DNS), une fois de temps en temps, la première requête obtiendra `1.1.1.1` comme réponse et la deuxième obtiendra `127.0.0.1`.

![entrées dns](dns_entries.png)

Après, on n'a qu'à envoyer l'URL `http://<domaine>/maintenance.php` et avec un peu de chance, on reçoit le flag via l'erreur.

![success](success.png)

## Flag
`flag-C3tteL1gn3DAtt3nt3EstR1d1cul3m3n7L0ngu3`