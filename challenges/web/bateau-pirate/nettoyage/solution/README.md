# Nettoyage

## Write-up (français)

Le défi parle de nettoyage, donc on peut déduire que le défi à un lien avec l'apparence du site web.

Lorsqu'on regarde le code source de la page [`nettoyage`](../../src/templates/nettoyage.html) (clic droit `View Page Source`).

On s'aperçoit que le flag est écrit dans la balise `p` en clair. C'est le css qui le cache avec `visibility: hidden;`.

Une autre manière d'inspecter le code c'est avec les DevTools:

1. Aller sur la page du défi [`peinture`](../../src/templates/peinture.html)
2. Ouvrir les DevTools en appuyant sur F12 ou clic droit `Inspect`
3. Sélectionner dans l'onglet en haut des DevTools `Inspector`
4. Ouvrir les balises html `body`, `div` et `p`

## Write-up (english)

The challenge talks about cleaning, so we can deduce that the challenge has to do with the appearance of the website.

When looking at the source code of the [`cleaning`](../../src/templates/cleaning.html) page (right click `View Page Source`).

We can see that the flag is written in the `p` tag in plain text. It's the css that hides it with `visibility: hidden;`.

One way to inspect code is with DevTools:

1. Go to the challenge page [`painting`](../../src/templates/painting.html)
2. Open DevTools by pressing F12 or right click `Inspect`
3. Select in the tab at the top of the DevTools `Inspector`
4. Open `body`, `div` and `p` html tags

## Flag

`flag-N0T-T0T411Y-5P1CK-N-5P4N`
