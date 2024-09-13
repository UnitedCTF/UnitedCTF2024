# Stand de tir 3
## Write-up
Dans ce défi, le jeu de données a été créé en plaçant 10 points aléatoirement dans un espace 8D avec des axes restreints entre 0 et 1. La principale différence par rapport au défi précédent est l'utilisation d'une fonction de distance *custom*. Voici son implémentation en Python :
```python
def distance_custom(p1: Sequence, p2: Sequence):
    return sum((
        abs(p1[0] - p2[0]),
        2*abs(p1[1] - p2[1]),
        (p1[2] - p2[2])**2,
        abs(p1[3] - p2[3]),
        (p1[4] - p2[4])**2,
        abs(p1[5] - p2[5]),
        3*abs(p1[6] - p2[6]),
        abs(p1[7] - p2[7]),
    ))
```  
Encore une fois, il se résoud bien avec un KNN, mais cela nécessite d'utiliser la distance custom. Sinon, d'autres algorithmes ont été testés et donnent la bonne réponse aussi, comme un [classificateur par machines à support de vecteur](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC) ou le fameux [perceptron multicouche](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier), quoi qu'ils enlèvent peut-être le fun de la chose.