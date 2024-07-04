# CYBEAR SECURITY Lv3

## Write-up (français)

On peut voir que le braille a été remplacé par le message "NO MORE DOTS". Il faudra trouver une autre manière de trouver l'ordre de ballons.

Ce défi est toujours en lien avec le braille. Si vous connaissez déjà le fonctionnement de numérotation des "dots", vous avez la réponse. Sinon :  

On remarque que chaque ballon a maintenant un système d'identification commençant par "3456". Avec un peu de recherche avec "3456 braille" ou quelque chose du genre, vous trouverez que "3456" correspond au symbole "⠼". Pourquoi ?

En Braille, les "dots" font référence aux positions des points d'une cellule Braille comme la suivante :
1 ● ● 4
2 ● ● 5
3 ● ● 6

Ainsi, il est maintenant possible de décoder chaque identification en un nombre unique allant de 1 à 12.

3456-15 = ⠼⠑ = 5 => 7    3456-1245 = ⠼⠛ = 7 => n     3456-12 = ⠼⠃ = 2 => 0
3456-125 = ⠼⠓ = 8 => g   3456-1-12 = ⠼⠁⠃ = 12 => s   3456-14 = ⠼⠉ = 3 => u
3456-24 = ⠼⠊ = 9 => d    3456-1 = ⠼⠁ = 1 => c        3456-1-1 = ⠼⠁⠁ = 11 => 7
3456-124 = ⠼⠋ = 6 => 1   3456-145 = ⠼⠙ = 4 => n      3456-1-245 = ⠼⠁⠚ = 10 => 0

On note les caractères et en les ordonnant selon les nombres, on obtient le flag !

c(1) 0(2) u(3) n(4) 7(5) 1(6) n(7) g(8) d(9) 0(10) 7(11) s(12)

flag-c0un71ngd07s

## Write-up (english)

We can see that the previous Braille has been replaced with the message "NO MORE DOTS". We will need to find another way to get the balloon order.

This challenge is still related to Braille. If you already know how the "dot" system works, then you probably already know what to do. If not :

We notice that each balloon is now identified with a number pattern starting with "3456". After some research of things like "3456 braille", you will find that "3456" corresponds to "⠼" in Braille. Why ?

In Braille, the "dots" are a reference to their positions within a Braille cell such as the following :
1 ● ● 4
2 ● ● 5
3 ● ● 6

We can now decode each identification into a unique number from 1 to 12.

3456-15 = ⠼⠑ = 5 => 7    3456-1245 = ⠼⠛ = 7 => n     3456-12 = ⠼⠃ = 2 => 0
3456-125 = ⠼⠓ = 8 => g   3456-1-12 = ⠼⠁⠃ = 12 => s   3456-14 = ⠼⠉ = 3 => u
3456-24 = ⠼⠊ = 9 => d    3456-1 = ⠼⠁ = 1 => c        3456-1-1 = ⠼⠁⠁ = 11 => 7
3456-124 = ⠼⠋ = 6 => 1   3456-145 = ⠼⠙ = 4 => n      3456-1-245 = ⠼⠁⠚ = 10 => 0

We note the characters and by ordering them with their number, we get the flag !

c(1) 0(2) u(3) n(4) 7(5) 1(6) n(7) g(8) d(9) 0(10) 7(11) s(12)

flag-c0un71ngd07s