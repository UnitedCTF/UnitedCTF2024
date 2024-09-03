# Park terminal

En naviguant sur la page web, on peut voir que le terminal est géré par un script PHP.
Il est indiqué que nous n'avons pas les permissions requises pour obtenir un ticket.

On peut donc supposer que notre session n'a pas les droits requis.
En PHP, les session sont stocké par défaut dans un dossier temporaire
https://stackoverflow.com/questions/4927850/location-for-session-files-in-apache-php.

En listant les fichiers du dossier `/tmp`, on voit plusieurs sessions existantes sur le serveur.

```
sess_0d2ab5e7894135660f19c6b0c260b643	0
sess_65a1588c37413024440677c186380d9b3	22
sess_75a1588c37430244940677c186380d9b3	22
sess_4a7d1ed4144674e4033ac29ccb8653d9b	22
sess_55a1588c37463024440677c186380d9b3	22
sess_15a1588c37430224440677c186380d9b3	22
sess_95a1588c37430241440677c186380d9b3	22
sess_45a1588c37423024440677c186380d9b3	22
sess_85a1588c37430244540677c186380d9b3	22
sess_25a1588c37430024440677c186380d9b3	22
sess_35a1588c37493024440677c186380d9b3	22
```

On peut essayer les différentes sessions pour voir si l'une d'elles nous donne les droits requis.

En modifiant le cookie de session avec l'une des sessions existantes et en explorant la racine du 
terminal, on peut voir de nouveaux fichiers et dossiers qui n'étaient pas accessibles auparavant.

```
sess_65a1588c37413024440677c186380d9b3
```

Une fois cette session utilisée, on peut voir le fichier `.flag-HoHoPHPOupsiiii` à la racine du terminal.



## Flag

`flag-HoHoPHPOupsiiii`
