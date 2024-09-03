# Fortune L33t3r

## Write-up

Le principe est le même que pour le challenge précédent, mais la nouvelle difficulté est qu'un symbole LeetSpeak peut être utilisé pour encoder différentes lettres.

### Correspondance 1:1

Certains symboles LeetSpeak correspondent à une seule lettre en clair. Dans ce cas-là, la solution est la même que dans le challenge précédent.

```python
{
    '4': 'a',
    '3': 'e',
    '9': 'g',
    '0': 'o',
    '5': 's',
    '2': 'z'
}
```

### Correspondance 1:n

Certains symboles LeetSpeak correspondent désormais à plusieurs lettres en clair, ce qui rend le décodage non-déterministe.

```python
{
    '1' : ["i", "l"],
    '7' : ["t", "y"],
    '<|': ["d", "q"],
    '\/': ["u", "v"]
}
```

Par exemple, le LeetSpeak `<|475` peut correspondre à 4 "mots" différents : `dats`, `days`, `qats` et `qays`

Pour palier à ce problème, on va générer tous les mots possibles puis on va regarder ceux qui existent en anglais. J'ai utilisé [un grand dictionnaire anglais](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) afin d'éviter les faux négatifs.

Si parmi les mots générés, plusieurs sont présent dans la langue anglaise, alors on va choisir le mot le plus probable à l'aide d'un [deuxième dictionnaire](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears.txt) plus restreint et rangé par ordre de fréquence.

Dans le cas (assez improbable) où aucun des mots générés n'est dans le premier dictionnaire, alors on demande à l'utilisateur de choisir (rapidement) le meilleur.

Certains rares cas de figure peuvent produire des erreurs (comme les contractions avec des apostrophes telles que `you'll`) mais ce script fonctionne assez bien.


## Flag

`flag-Th3F0r7un3C00ki3IsN07ALi3`
