# Stand de tir 1

**`Auteur`** [Bonsoir](https://github.com/florentduchesne)

![Cible](cible.jpg)

## Description (français)

Vous venez de trouver votre premier emploi au parc d'attractions (félicitations)!
Après tant d'années d'études, vous êtes finalement arrivé à la conclusion que le marché de l'emploi n'est tout simplement pas ce qu'on vous a vendu. Par chance, d'autres options s'offrent à vous, comme le commerce des chaussons aux pommes ou les emplois étudiants. Grâce à vos contacts, vous avez déniché le nouvel emploi de vos rêves: le poste d'adjoint à la direction des activités d'addresse et de dextérité du parc. En d'autres mots, vous êtes derrière un stand de tir, commencez patiemment votre formation.

On vous présente des cibles annotées; vous voyez une série de trous (coordonnées) sur une feuille (un plan 2D), chacun associé à un score allant de 0 à 10. On vous présente ensuite une nouvelle feuille avec des points qu'on vous demande d'annoter.  
S'il vous est difficile d'établir une règle générale à l'aide d'un nuage de points, il y a sans doute quelque chose à faire à l'aide de ces données. Peut-être qu'il serait possible de comparer un point à ses plus proches voisins pour déterminer sa valeur?

Pour ce défi vous sont fournis deux fichiers CSV; le premier contient un ensemble de coordonnées 2D auxquelles sont à chacune associée un score. Il s'agit de votre jeu de données d'entraînement. Le second fichier contient uniquement un ensemble de coordonnées. Il s'agit de votre jeu de données d'évaluation. Vous souhaitez évaluer le score de chacune des coordonnées du jeu d'évaluation.

Les coordonnées sont contenues entre zéro et un. Pour ce que vous en savez, l'espace autour de vous vous semble euclidien. Il serait donc adéquat de calculer les distances ainsi.

**Format du flag**: `flag-[0-9]{20,40}`

Le flag est une concaténation du score de tous les points du jeu de test dans l'ordre. Par exemple, si votre jeu de test comporte trois points valant 8, 4 et 10 respectivement, votre flag sera `flag-8410`.

**Données d'entraînement**:  
![Data_challenge_1](Data_challenge_1.png)  
**Données de test**:  
![Data_challenge_1_test](Data_challenge_1_test.png)  

## Description (english)

You have just found your first job at the amusement park (congratulations)! After many years of study, you have finally come to the conclusion that the job market is not exactly what you were sold. Fortunately, other options are available to you, such as pastry-making or student jobs. Thanks to your contacts, you have landed your dream job: the position of Assistant Director of Address and Dexterity Activities at the park. In other words, you are behind a shooting stand, so start your training patiently.

You are presented with annotated targets; you see a series of holes (coordinates) on a sheet (a 2D map), each associated with a score ranging from 0 to 10. You are then given a new sheet with points that you need to annotate.
If it's difficult for you to establish a general rule with a cloud of points, there is likely something you can do with this data. Perhaps it would be possible to compare a point to its nearest neighbors to determine its value?

For this challenge, you are provided with two CSV files; the first contains a set of 2D coordinates each associated with a score. This is your training dataset. The second file contains only a set of coordinates. This is your evaluation dataset. You want to assess the score of each coordinate in the evaluation dataset.

The coordinates range between zero and one. As far as you know, the space around you seems Euclidean. Therefore, it would be appropriate to calculate distances this way.

**Flag format**: `flag-{[0-9]{20,40}}`

The flag is a concatenation of the score of all the datapoints from the test set, in order. e.g., if your test dataset has three points worth 8, 4 and 10 points each, your flag should be `flag-8410`.

## Solution

La solution du défi peut être trouvée [ici](solution/).