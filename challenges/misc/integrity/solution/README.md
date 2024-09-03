# Integrite

## Write-Up

On se rend compte que Marc a "malencontreusement" mis en danger l'intégrité de son mot de passe.
Dans l'archive Git, on peut voir que chaque commit a été augmenté avec un hash d'intégrité pour 
une ébauche d'automatisation maison. On y retrouve le script. On peut donc créer un script pour 
vérifier si l'un des commits n'a pas la bonne intégrité.

```sh
#!/bin/bash

cd "integrity"

git log --pretty=format:"%H %s" | while read commit_hash commit_message; do
  integrity_hash=$(echo $commit_message | awk '{print $NF}')


  git checkout  "$commit_hash"

  file_hash="$(md5sum readme.md | awk '{ print $1 }')"

  if [ "$integrity_hash" != "$file_hash" ]; then
    echo "$integrity_hash n'est pas valide vs $file_hash"
    exit 0
  fi
done
```

On constate que le hash `3c2234a7ce973bc1700e0c743d6a819c` n'est pas valide selon notre script. 
Comme nous cherchons le mot de passe de Marc, nous supposons que ce hash invalide est en fait son 
mot de passe. En effectuant une recherche sur Internet (https://md5decrypt.net/en/), nous trouvons 
que le mot de passe est : `metallica`.


## Flag

`flag-d0nT5HarEy0urP@s5owRd`