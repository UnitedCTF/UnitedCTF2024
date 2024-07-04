# CYBEAR SECURITY Lv4

## Write-up (français)

Pour réussir ce défi, le meilleur indice est le message "WIN BIG OR GET DUXBURIED".

On commence par faire une recherche sur ce qu'est "duxbury" ... "duxbury Braille" jusqu'à comprendre qu'il s'agit d'un méthode d'écriture abrégée.

En fouillant sur internet, il est possible de trouver des chartes de traductions comme ueb_black8.pdf.

Si on observe les étiquettes des ballons :
23-l    23-l    23-f    26
23-l    af      af      23-l
af      abv     abv     23-f
af      23-f    af      abv

On peut comparer avec notre charte pour trouver : 
abv = above (en haut)
af = after (après)

Qu'en est-il de 23-f et 23-l ?

On se rappel que les nombres correspondent à des positions (⠆). On continue de chercher 
⠆l et ⠆f (ou encore ⠆⠇ et ⠆⠋) pour trouver :

abv = above (en haut)
23-l = below (en bas)
23-f = before (avant)
af = after (après)
26 = ⠢ = enough (assez) *Il est possible de trouver le flag sans traduire "26"

Ces étiquettes servent donc d'indications d'un chemin à travers les ballons. Le ballon rouge est notre point de départ.

m      c      3      y
▼      ▼      ◄    assez

y      8      3      4
▼      ►      ►      ▼

c      y      s      r
►      ▲      ▲      ◄

r      u      1      t
►      ◄      ►      ▲

On note les caractères dans l'ordre (en passant par dessus les ballons déjà éclatés).

flag-mycy834rs3cur1ty

## Write-up (english)

The biggest hint as to how to start this challenge is the "WIN BIG OR GET DUXBURIED" message.

After researching "duxbury" or "duxbury braille", you can learn that duxbury is a form of abbriged Braille.

You can now look for a translation chart such as ueb_black8.pdf.

If we take a look at the balloons tags :
23-l    23-l    23-f    26
23-l    af      af      23-l
af      abv     abv     23-f
af      23-f    af      abv

We can compare these with our chart to find : 
abv = above
af = after

What about 23-f and 23-l ?

We remember that numbers correspond to dot positions (⠆). We keep looking for
⠆l and ⠆f (or ⠆⠇ and ⠆⠋) to find :

abv = above
23-l = below
23-f = before
af = after
26 = ⠢ = enough *You can get the flag without finding this one.

The tags serves as path directions to pop the balloons. The red balloon is our starting point.

m      c      3      y
▼      ▼      ◄    enough

y      8      3      4
▼      ►      ►      ▼

c      y      s      r
►      ▲      ▲      ◄

r      u      1      t
►      ◄      ►      ▲

We note the characters in the order (skipping already popped balloons).

flag-mycy834rs3cur1ty