# CYBEAR SECURITY Lv2

## Write-up (français)
Pour réussir ce défi, on commence par détecter le Braille sur le panneau (en haut à gauche).

Ensuite, si on ne sait pas comment le lire, une petite recherche de "cheatsheet" ou de charte Braille comme braille_cheatsheet.jpg permet d'analyser le message. 

L'indicateur "⠼" informe la présence de nombres. On traduit chaque nombre pour voir qu'ils se trouvent entre 1 et 16, soit, le nombre de ballons.

⠼⠁⠑=15 ⠼⠋=6 ⠼⠓=8 ⠼⠃=2 ⠼⠁=1 ⠼⠑=5
⠼⠁⠃=12 ⠼⠁⠚=10 ⠼⠁⠉=13 ⠼⠊=9 ⠼⠁⠙=14
⠼⠙=4 ⠼⠁⠋=16 ⠼⠁⠁=11 ⠼⠛=7 ⠼⠉=3

Chaque nombre correspond à une position de ballon. Il ne reste plus qu'à noter les caractères des ballons selon l'ordre du Braille (en minuscules, tel qu'indiqué dans la description du défi):

15=y 6=0 8=u 2=f 1=3 5=l
12=t 10=7 13=h 9=3 14=4
4=n 16=s 11=w 7=3 3=r

flag-y0uf3lt7h34nsw3r

## Write-up (english)
To do this challenge, you first need to notice the Braille writing in the upper left corner.

Then, if you can't read Braille, you can search online for a Braille "cheatsheet" or "chart" to find something like the braille_cheatsheet.jpg to analyze the message.

The "⠼" indicator tells you that the Braille is a bunch of numbers. We can now use our chosen reference to translate our Braille as such :

⠼⠁⠑=15 ⠼⠋=6 ⠼⠓=8 ⠼⠃=2 ⠼⠁=1 ⠼⠑=5
⠼⠁⠃=12 ⠼⠁=10 ⠼⠁⠉=13 ⠼⠊=9 ⠼⠁⠙=14
⠼⠙=4 ⠼⠁⠋=16 ⠼⠁⠁=11 ⠼⠛=7 ⠼⠉=3

We notice that each number is different and they go from 1 to 16. 16 is the exact number of balloons shown, indicating that each number corresponds to a balloon position. We finally take our noted numbers and replace each with a character from the corresponding balloon (in lowercase).

15=y 6=0 8=u 2=f 1=3 5=l
12=t 10=7 13=h 9=3 14=4
4=n 16=s 11=w 7=3 3=r

flag-y0uf3lt7h34nsw3r