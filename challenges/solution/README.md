# Circus

## Write-up (français)

Indépendamment de la personne qu'on prends pour se connecter au VM, il y a des indices pour dire quel compte prendre pour ensuite trouver un fichier caché.
L'incide dans le fichier parle d'un lapin et de son nom, le lapin fait référence à la cryptographie "RABBIT" et le mot de passe de chiffrement est une chaîne 16 de caractère
qui se trouve être le nom du compte répété 2 fois comme l'indice le dit.

ATTENTION, l'un des fichiers TXT est une piège, le lapin décider de poser un lapin ;)

On peut donc utiliser [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)Rabbit(%7B'option':'UTF8','string':'BarnabasBarnabas'%7D,%7B'option':'Hex','string':''%7D,'Big','Raw','Raw')&input=SHpNWDQrMXhzeXFJVzYrdXl2K0JVNWI4STB3aVBPUT0&oeol=FF) pour décoder la solution.

## Write-up (english)

Regardless of who you take to log into the VM, there are clues to tell which account to take and then find a hidden file.
The hint in the file talks about a rabbit and its name, the rabbit refers to cryptography "RABBIT" and the encryption password is a 16 character string
which happens to be the account name repeated 2 times as the hint says.

So we can use [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)Rabbit(%7B'option':'UTF8','string':'BarnabasBarnabas'%7D,%7B'option':'Hex','string':''%7D,'Big','Raw','Raw')&input=SHpNWDQrMXhzeXFJVzYrdXl2K0JVNWI4STB3aVBPUT0&oeol=FF) to decode the solution.

ATTENTION, one of the TXT files is a trap, the rabbit decides to stand someone up ;)

## Flag

`flag-g0745uRpRI53f0Ry0u`
