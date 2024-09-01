# Peinture

## Write-up (français)

Le défi parle `réfléchir sur ce qui est important`. Pour les pirates, les trésors sont quelque chose d'important.
On voit sur la page un trésor en arrière plan.

Lorsqu'on regarde le code source de la page [`citation`](../../src/templates/citation.html) (clic droit `View Page Source`), on voit un [fichier css](../../src/static/css/style-citation.css):
`<link rel="stylesheet" type="text/css" href="/static/css/style-citation.css">`.

Il est possible de double cliquer sur le lien `/static/css/style-peinture.css` pour accéder au fichier.

On s'aperçoit que le nom du fichier pour arière-plan est `flag-3Y35-0N-TH3-PR1Z3`

Une autre manière d'inspecter le code c'est avec les DevTools:

1. Aller sur la page du défi [`citation`](../../src/templates/citation.html)
2. Ouvrir les DevTools en appuyant sur F12 ou clic droit `Inspect`
3. Sélectionner dans l'onglet en haut des DevTools `Inspector`
4. Ouvrir la balise html `head`
5. Double cliquer sur le lien `/static/css/style-peinture.css` pour accéder au fichier.

## Write-up (english)

The challenge is about `reflect on what is important`. For pirates, treasures are something important.
We see on the page a treasure in the background.

When we look at the source code of the page [`citation`](../../src/templates/citation.html) (right click `View Page Source`), we see a [fichier css](../../src/static/css/style-citation.css):
`<link rel="stylesheet" type="text/css" href="/static/css/style-citation.css">`.

It is possible to double click on the link `/static/css/style-peinture.css` to access the file.

We can see that the name of the file for the background is `flag-3Y35-0N-TH3-PR1Z3`

Another way to inspect code is with DevTools:

1. Go to the challenge page [`citation`](../../src/templates/citation.html)
2. Open DevTools by pressing F12 or right click `Inspect`
3. Select in the tab at the top of the DevTools `Inspector`
4. Open the html `head` tag
5. Double click on the link `/static/css/style-peinture.css` to access the file.

## Flag

`flag-3Y35-0N-TH3-PR1Z3`
