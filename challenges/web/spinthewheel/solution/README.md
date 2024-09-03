# Roue de fortune

## Write-up

### Probabilités

Le défi nous présente une roue de fortune qu'on peut faire tourner sans arrêt. À chaque fois qu'elle tourne, elle a 5 chances sur 12 de faire un gain, 4 chances sur 12 de ne pas faire de gain et 3 chances sur 12 de tout perdre.

Puisque le plus haut prix de la roue est 20$ et qu'il nous faut 10,000$ pour obtenir le flag, nos chances de gagner assez d'argent pour avoir le flag sont de (3/4)^500 dans le meilleur cas, mais en réalité elles sont encore plus basses.

Nous pouvons donc comprendre que gagner assez d'argent par la force brute est tout simplement irréaliste.

### Analyse

En jouant un peu avec le site et en observant les requêtes au serveur, on peut faire quelques observations.

- Il n'y a que trois endpoints visibles, la racine `/`, la page de rédemption `/redeem` et l'appel utilisé pour faire tourner la roue `/spin`.
- Un cookie nous est envoyé de la part du serveur, du nom de `session` et contenant un payload JSON. Le cookie contient aussi une signature et un hash. On peut reconnaitre que c'est un cookie émis par Flask par son format.

Le payload JSON a l'air de ceci:

```json
{"balance":10,"uid":{" u":"e2b6cd8502474bc49d385d2486594bfb"}}
```

Il faut mentionner que puisque le cookie est signé par le serveur, il n'est pas possible de tout simplement modifier notre balance, même s'il est possible de la consulter.

### Solution

Dû à la nature des cookies de session émis par Flask, un cookie demeure valide même si la session concernée a été modifiée.

En effet, Flask gère les cookies de session comme suit (brièvement):

1. Les données du cookie de session sont décodées de base64.
2. La signature du cookie est vérifiée (voir [itsdangerous](https://itsdangerous.palletsprojects.com/en/2.2.x/url_safe/)).
3. Les données utiles forment un objet JSON créé dans un format propre à Flask ([Tagged JSON](https://github.com/pallets/flask/blob/a8956feba1e40105e7bc78fa62ce36c58d1c91e1/src/flask/json/tag.py)), ce format restreint énormément les types d'objets qui peuvent être créés.

Comme nous pouvons le constater, Flask n'a pas de mécanisme pour identifier la version la plus récente d'un cookie de session. Ça fait en sorte que l'on peut réutiliser une vieille version du cookie de session émise par le serveur si on le veut.

Dans le cas du challenge, on peut:

1. Faire une sauvegarde de notre cookie.
2. Faire tourner la roue.
3. **Si** on a gagné, on retourne à l'étape 1.
4. **Sinon**, on ignore le nouveau cookie envoyé par le serveur en faveur du cookie qu'on a sauvegardé auparavant et on retourne à l'étape 1.

Étant donné qu'il faut répéter cette séquence jusqu'à ce qu'on se rende à 10,000$, il est préférable d'automatiser la procédure avec un script. Voir [solver.py](solver.py)

## Flag
`flag-Fl4skNS7uff`