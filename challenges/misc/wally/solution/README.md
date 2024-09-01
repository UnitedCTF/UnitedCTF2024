# Wally

## Write-up

Le nom du défi fait référence à Wally la baleine. La personne doit faire un lien docker et la baleine. 
Avec Docker, il est possible d'importer une image à partir d'un fichier tar. 

```
docker load  -i wally.tar
```

L'image se trouve à la racine du container, donc il est possible de l'avoir avec les commande suivantes :

Pour partir le container en interactif.
```
docker run -it wally
```

Pour copier l'image en local.
```
docker cp <container ID>:/ticket.png <local paths>/
```

En lisant le contenu de l'image, on trouve le flag `flag-Th3Wh4l3AteMyT1ck3t`.