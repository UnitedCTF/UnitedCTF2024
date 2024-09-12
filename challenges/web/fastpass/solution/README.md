# Fastpass 1

## Write-up (français)

1. Aller sur /health comme suggéré nous redirige vers /actuator/health. Cela est un indice que le site utilise les actuators de Spring.
2. On peut donc tous les essayer en cherchant une liste sur le web. On trouve que /actuator/env fonctionne.
3. Dans la liste, on trouve FTPUSER=ubuntu et FTPPASSWORD, qui est le flag.

## Write-up (english)

1. Going to /health as suggested redirects us to /actuator/health. This is a clue that the site uses Spring actuators.
2. You can try them all by searching the web for a list. We find that /actuator/env works.
3. In the list, we find FTPUSER=ubuntu and FTPPASSWORD, which is the flag.

`flag-4ctu4t0r5-ftw-a6c331fd0`

# Fastpass 2

## Write-up (français)

1. En utilisant les identifiants obtenus, on se connecte via ftp au port 21
2. On fait `ls -slart` pour voir les fichiers cachés.
3. Le flag se trouve dans le fichier commençant par `.vip`.

## Write-up (english)

1. Using the identifiers obtained, connect via ftp to port 21
2. Do `ls -slart` to see the hidden files.
3. The flag is in the file starting with `.vip`.

`flag-y0u-f0und-th3-f4stp455-79f3d12`

# Fastpass 3

## Write-up (français)

1. On remarque l'existence du dossier .ssh/
2. Le fichier authorized_keys peut être remplacé par un fichier que nous créons avec notre clé publique (ftp put)
3. On peut alors se connecter en SSH sur le port 22.
4. `sudo -l` nous montre qu'on peut utiliser python3 en tant que root.
5. import os
6. os.system("cat /root/key.txt")
7. La localisation de la clé était indiqué dans le fichier .csv du deuxième flag.


## Write-up (english)

1. Note the existence of the .ssh/ folder.
2. The authorized_keys file can be replaced by a file that we create with our public key (ftp put)
3. We can then connect via SSH on port 22.
4. `sudo -l` shows us that we can use python3 as root.
5. import os
6. os.system("cat /root/key.txt")
7. The location of the key was indicated in the .csv file in the second flag.

`flag-go-enjoy-the-rides-995cc32a`

# Fastpass Rebooted

## Write-up (français)

1. Le service API Spring fonctionne sous l'utilisateur root.
2. Remplacer le fichier jar exécuté par le service par un exécutable permettant l'escalade de privilège est la clé du défi.
3. Il faut ensuite redémarrer le conteneur depuis le instanceur pour que le service redémarre aussi sans avoir besoin de permissions root pour ce faire.


## Write-up (english)

1. The API Spring Service runs as the root user.
2. Replacing the jar file executed by the service with an executable that can allow privilege escalation is the key to the challenge.
3. The container must then be restarted with the Instancer, so that the service will aslo restart, without needing to be root to do so.

`flag-wh4t-a-r0ll3r-c04st3r-111a13`
