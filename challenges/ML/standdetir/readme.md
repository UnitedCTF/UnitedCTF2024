# Stand de tir 1

**`Auteur`** [Bonsoir](https://github.com/florentduchesne)

![Cible](cible.jpg)

## Description (français)

Finalement un endroit calme! Le parc d'attractions était tellement bruyant et tellement mouvementé, vous avez entrepris il y a quelque temps de vous éloigner de tout. Défilant à gauche et à droite à la recherche d'un endroit où respirer, vous avez découvert une allée pour le moins étrange; les bruits des manèges ne semblent pas résonner jusqu'ici, et il vous est impossible de vous souvenir du chemin que vous avez pris pour y arriver. Avec un soupir de soulagement, vous profitez pour un moment du calme ambiant, espérant que cela ne se termine jamais.
Après quelque temps, vous réalisez que l'allée n'est pas aussi vide qu'il n'y paraît; un stand de tir, fameuse attrappe à touristes, vous fait faice. Vous vous en approchez sous les yeux émerveillés d'un vieillard derrière le comptoir.
« Finalement! De la chair fraîche! », vous lança-t-il. « Je suis seul ici depuis... depuis... ».
Vous regardez autour de vous; il n'y a effictivement pas un chat dans les parages.
« J'ai oublié, mais qu'importe, je peux finalement me faire remplacer! Il est grand temps de prendre ma retraite. »

Si vous n'étiez pas au courant, il est coutûme dans ce parc d'attractions de trouver son remplaçant avant de quitter son poste. Vous n'avez pas le choix.

Alors que vous vous empressez de prendre votre place, vous voyez le vieillard sortir une valise de derrière le comptoir. Il vous montre une photo en tons de gris; « Voyez-vous, j'ai un chat qui m'attend à la maison, et je ne l'ai pas nourri depuis le début de mon quart. Je vous souhaite bonne chance! ».

Solitude.

Comme vous avez un peu de temps à tuer, vous décidez de faire un inventaire de votre tout nouveau stand. Vous trouvez quelques feuilles de cibles de tir neuves et usagées qui traînent un peu partout. Vous vous pratiquez à quelques reprises sur les feuilles neuves, mais remarquez vite un problème; les différentes zones de chaque cible ne sont pas annotées, il vous est donc impossible de déterminer votre score! Horreur! À quoi bon viser au milieu d'une cible si aucun chiffre n'y est attaché? Vous avez besoin de métriques, il vous *faut* une manière numérique de comparer vos performances à celle du commun des mortels. Sinon, impossible de prouver votre supériorité.

Par chance, en jetant un coup d'oeil plus approfondi aux cibles usées, vous remarquez quelque chose; votre prédécesseur a annoté de nombreux trous avec des chiffres allant de -1 à 10. S'il vous est difficile d'établir une règle générale à l'aide d'un nuage de points, il y a sans doute quelque chose à faire à l'aide de ces données. Peut-être qu'il serait possible de comparer un point à ses plus proches voisins pour déterminer sa valeur?

Pour ce défi vous sont fournis deux fichiers CSV; le premier contient un ensemble de coordonnées 2D auxquelles sont à chacune associée un score. Il s'agit de votre jeu de données d'entraînement. Le second fichier contient uniquement un ensemble de coordonnées. Il s'agit de votre jeu de données d'évaluation. Vous souhaitez évaluer le score de chacune des coordonnées du jeu d'évaluation.

Les coordonnées sont contenues entre zéro et un. Pour ce que vous en savez, l'espace autour de vous vous semble euclidien. Il serait donc adéquat de calculer les distances ainsi.

À vue d'oeil, ils vous semble approprié de dire que `k` est égal à 3.

**Aucun chat n'a été blessé durant la rédaction de cette mise en situation**

**Format du flag**: `flag-{base64(la somme du score de tous les points du jeu d'évaluation)}`


## Description (english)

See above.


## Solution

La solution du défi peut être trouvée [ici](solution/).