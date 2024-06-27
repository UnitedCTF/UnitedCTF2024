# Security through obskurity

## Write-up (français)

Pour résoudre le challenge, il faut en ignorer la majorité. Tu peux bien essayer de tout le comprendre, mais comme l'implique la description, t'as pas besoin. C'est une perte de temps : 60% du code est utilisé pour calculer un array constant (`s`) que tu peux juste copier-coller dans ta solution.

Tant que tu essaye pas de tout comprendre, le challenge est assez simple et direct: tu fais juste des allez-retours entre le code et la documentation.

J'assume que tu connais les bases de lire du K depuis [le tutoriel dans la description](https://razetime.github.io/ngn-k-tutorial/), mais comme petit rappel:
- tout est lu et exécuté de la droite vers la gauche.
- `a:b` est une affectation (`a = b` dans les autres languages)
- `{}` crée une fonction
- `f[a;b]` appelle la fonction `f` avec les arguments `a` et `b`

Le coeur de l'algorithme est la dernière ligne : `0{s@e[x;y]}\"flag-redacted"`. Contrairement à toutes les autres lignes, il ne s'agit pas d'une affectation, et le résultat est donc imprimé à la console. Le texte chiffré est exactement ce résultat.

En regardant le manuel, on peut voir plusieurs définitions de `\`. Comme il y a `0` à gauche de la fonction, et que la fonction utilise 2 arguments implicites (`x` et `y`) ce qui la rend "dyadic", nous avons affaire à `x F\`, un "seeded scan".

On peut donc dire que `s@e[x;y]` chiffre un charactère `y` du plaintext en connaissant `x`, le dernier charactère du message chiffré. Continuant de droite à gauche donc, on regarde maintenant la fonction `e:b/~=/b\',`, qui est équivalent à `e:{b/~=/b\'x,y}`.

`e` place d'abord ses arguments dans une liste à deux éléments en utilisant `,`, puis encode (`\`) chacun (`'`) en binaire (parce que `b` est défini comme `8#2`, une liste à 8 éléments remplie de 2). Nous pouvons déjà voir `b/` qui décode en retour (pas de each `'`, il y un seul résultat) à partir de binaire. D'après `~` (not) et `=` (equals), on peut deviner que cette fonction est l'opérateur binaire ou `e`xclusif.

La dernière partie de notre algorithme de "chiffrage" est donc `s`. Comme indiqué plus haut, vous n'êtes pas censé essayer de comprendre cette partie. Si vous essayez d'évaluer `s`, et peut-être `#s`, vous verrez qu'il s'agit d'une liste de 256 éléments contenant les entiers de 0 à 255. C'est une permutation, ou en d'autres termes, une boîte de substitution (S-box). Pour déchiffrer, on a pas besoin de savoir comment `s` a été calculé, on doit simplement inverser la permutation.

Si on veut, on peut maintenant décrire mathématiquement notre algorithme (on en a vraiment pas besoin pour un algorithme si simple, mais c'est bonne pratique néanmoins) :
$$e_i = S(m_i \oplus e_{i-1})$$

Et trouver la valeur de $m$ en fonction de $e$:
$$\begin{align*}
m_i &= m_i \oplus 0
\\&= m_i \oplus (e_{i-1} \oplus e_{i-1})
\\&= S^{-1}(S(m_i \oplus e_{i-1})) \oplus e_{i-1}
\\&= S^{-1}(e_i) \oplus e_{i-1}
\end{align*}$$

Tout ce que reste est d'écrire le script de déchiffrage. Si t'en as assez du K, il y a une solution en Python [ici](decrypt.py), mais faisons-le en K pour le plaisir.

La façon la plus évidente d'inverser la S-box serait peut-être de trouver l'index de chaque valeur de 0 à 255 (`s?/:!256`) mais il y a un [idiome plus pratique](https://mlochbaum.github.io/BQN/doc/order.html#ordinals) pour inverser une permutation dans les array langages comme K; on a juste besoin de trier : `<s`.

En K, l'opérateur `@` nous permet d'obtenir les valeurs à plusieurs indices à la fois, donc `(<s)@encrypted` passera le texte chiffré entier à travers la S-box inverse en une seule opération. Ensuite, on décale le texte chiffré et on ajoute un zéro : `0,-1_encrypted`. On peut réutiliser la fonction `e` que nous avons déjà pour xor. `(0,-1_encrypted)e'(<s)@encrypted` est tout ce qu'il faut pour déchiffrer.

...mais à moins que vous connaissez la table ASCII par coeur, la vraie dernière étape sera de transtyper (`$`) la liste des valeurs d'octets en une chaîne de caractères :

```
`c$(0 :':encrypted)e'(<s)@encrypted
```

## Write-up (english)

The intended way to solve this challenge is to ignore most of it. You very well could try and understand it all, but as the description implies, you don't need to. It's a waste of time: over 60% of the code is used to calculate a constant array (`s`) you can simply copy-paste into your solution with no worry.

The rest of the challenge should be fairly straightforward, just go back and forth between documentation and the code.

I'll assume you know how the basics of reading K from [the tutorial linked in the description](https://razetime.github.io/ngn-k-tutorial/), but as a short summary:
- with a few exceptions, everything is executed and read from right to left
- `a:b` is variable assignment (`a = b` in other languages)
- `{}` makes a function
- `f[a;b]` calls function `f` with arguments `a` and `b`

The meat of the algorithm is the last line: `0{s@e[x;y]}\"flag-redacted"`. Unlike every other line, this isn't an assignment, and thus it prints its result. It's what gives us the ciphertext.

Looking at the manual, we can see multiple definitions of `\`. Seeing as there's `0` on the left of the function, and the function uses 2 implicit arguments (`x` and `y`) which makes it "dyadic", we're looking at `x F\`, a "seeded scan".

Thus, we can say that knowing `x`, the last character of the ciphertext, `s@e[x;y]` encrypts one character `y`. Going from right to left as usual, the next function to look at is `e:b/~=/b\',`, which is equivalent to `e:{b/~=/b\'x,y}`.

`e` first puts its arguments into a two-element list using `,`, then encodes (`\`) each (`'`) to binary (because `b` is defined as `8#2`, a 8-element list filled with 2). We can alreay see `b/` which decodes back (no each, a single result!) from binary. From `~` (not) and `=` (equals), you can hopefully guess this function is the `e`xclusive or bitwise operator.

The last part of our "encryption" algorithm then is `s`. As aforementioned, you aren't supposed to try to understand this part. If you try and evaluate `s`, and maybe `#s`, you'll see it's a 256-element list containing the integers from 0 to 255. It's a permutation, or in other words, a **substitution box**. To decrypt then, we won't need to know how `s` was calculated, we'll simply need to invert the permutation.

We can finally mathematically describe our algorithm as follows (we really don't need to for such a simple algorithm, but it's good practice regardless):
$$e_i = S(m_i \oplus e_{i-1})$$

And solving for our plaintext $m$ as a function of $e$:
$$\begin{align*}
m_i &= m_i \oplus 0
\\&= m_i \oplus (e_{i-1} \oplus e_{i-1})
\\&= S^{-1}(S(m_i \oplus e_{i-1})) \oplus e_{i-1}
\\&= S^{-1}(e_i) \oplus e_{i-1}
\end{align*}$$

All that's left is to write the decryption script. If you're boring there's a python solution [here](decrypt.py), but let's solve it in K for the hell of it.

The most obvious way to invert the S-box would perhaps be to find the index of every value from 0 to 255 (`s?/:!256`) but there is a [more convenient idiom](https://mlochbaum.github.io/BQN/doc/order.html#ordinals) to invert a permutation in array languages like K; you just need to sort: `<s`.

Array indexing `@` allows us to get the values at multiple indicies at once, so `(<s)@encrypted` will pass the entire ciphertext through the inverse S-box at once. Next, shift the ciphertext and add a zero: `0,-1_encrypted`. We can reuse the `e` function we already have for xor. `(0,-1_encrypted)e'(<s)@encrypted` is all it takes to decrypt.

...but unless you know the ASCII table by heart, the real last step will be to cast (`$`) the list of integer byte values to a string:

```
`c$(0 :':encrypted)e'(<s)@encrypted
```

## Flag

`flag-h0peUd1dntR34Dev3erything`
