# Émotions Fortes

## Write-up

## Niveau 1
On a trois catégories d'émotions, soit les positives, les négatives et les autres.

On ne peut pas résoudre ce défi à la main puisqu'il y a un timeout de 10 secondes et 10 rondes, donc on ne pourrait pas tomber sur la bonne réponse par chance (en tout cas, ça serait très peu probable de le faire 10 fois de suite).

En se connectant au défi et en catégorisant les émotions à la main, on peut trouver 39 émotions différentes qui sont assez faciles à catégoriser.

```python
CATEGORIES = [
    set("😢🥲😥😭😰😵🤕🤬😡🤢😫🤮💀"),
    set("😀😁🤣😄😎😆😋😍🤗😏😜😌🤪"),
    set("🥸🤡👽👻📎👺🤖🙊🦐🦭🦔💅🗿")
]
```

Une fois qu'on a les trois catégories, on peut se faire un petit script Python avec `pwntools` (ou pas) pour se connecter et trouver le parc avec une émotion de chaque catégorie.

Quelque chose du genre:

```python
for _ in range(10):
    parks = []

    r.recvuntil(b'es.\n\n')
    for _ in range(100):
        emotions = set(r.recvline().decode().strip()[4:].replace(' ', ''))
        parks.append(emotions)

    flag_park = [i+1 for i, park in enumerate(parks) if all([cat & park for cat in CATEGORIES])]

    r.recvuntil(b'> ')
    r.sendline(str(flag_park[0]).encode())
```

`flag-wwwwoo0ooOOOaAAa4ah`

## Niveau 2
Pour ce niveau, nous avons quelques représentants dans chaque catégorie, mais il n'y a pas de caractéristique évidente pour catégoriser le reste des visiteurs.

En se connectant au niveau et en comptant le nombre de visiteurs, on tombe sur 66. Ça serait ridicule d'essayer toutes les permutations de catégories possibles avec un nombre si haut, donc on doit essayer de compléter les catégories avec les informations que l'on a déjà.

Pour ce faire, nous utilisons la théorie des ensembles.

On peut représenter les visiteurs d'un parc par un ensemble. Puisque la grande majorité des parcs ont seulement des visiteurs de deux catégories (sauf celui qui en a trois), cet ensemble peut être vu comme une union de deux sous-ensembles des catégories.

```
Soit Vp (l'ensemble des visiteurs d'un parc), A et B (deux catégories).

Vp := A' ∪ B' où A' ⊆ A, B' ⊆ B
```

Si nous avons deux parcs avec une catégorie en commun, nous pouvons extraire tous les éléments de cette catégorie en commun.

```
Soit Vp1 et Vp2 (deux ensembles de visiteurs d'un parc avec une seule catégorie en commun), Vc (l'ensemble des visiteurs de cette catégorie dans les deux parcs en même temps)

Vc := Vp1 ∩ Vp2                      par définition
      (A'1 ∪ B'1) ∩ (A'2 ∪ C'2)     par définition
      A'1 ∩ A'2                      puisque A, B et C sont distincts
```

La procédure va donc comme suit:

1. À l'aide des représentants connus, nous tentons d'identifier les catégories présentes dans un parc. (nous ne préservons que les parcs avec deux catégories connues)
2. On considère une paire de ces parcs, qui ont une catégorie en commune et une catégorie distincte.
3. On extrait les visiteurs de cette catégorie à l'aide d'une intersection d'ensembles et on les ajoute aux représentants connus de la catégorie.
4. On répète le processus jusqu'à ce qu'on ait reconstitué les catégories (succès) ou qu'on ne soit plus capable de continuer (échec).

Une fois les ensembles reconstitués, la procédure est identique au premier niveau.

```
CATEGORIES = [
    set("😌🎃😓😀🦨😉🦔😜😨😥🤮😄🚴💀🥷😋😁🪲🤧🤗🎭😵"),
    set("🐉😎🙂🤪🐕😭🧸😊🤖😏😂🥲🦐😡📎🥸🙊😢👻🤡🗿😍"),
    set("💅🥴👺🤣👾😰🦩😈🦫😆😝😫🍭🤬😱😤🦭🐁🦆🤕🤢🐸")
]
```

`flag-s3tTh30ryMuch`