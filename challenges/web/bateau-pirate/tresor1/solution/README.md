# Captain

## Write-up (français)

Pour atteindre le flag, il faut écire la bonne clé dans le formulaire.

Lorsqu'on regarde le code source de la page [`tresor1`](../../src/templates/tresor1.html) (clic droit `View Page Source`), on voit un [fichier js](../../src/static/js/lvl1.js):
`<script src="/js/lvl1.js"></script>`.

Il est possible de double cliquer sur le lien `/js/lvl1.js` pour accéder au fichier.

On s'aperçoit que pour obtenir le flag dans une alerte (`alert(data['flag'])`), il faut écrire la bonne valeur de clé dans le formulaire (`document.getElementById('key').value`) en respectant la condition `if (key === "captain")`.

La clé a écrire dans le formulaire est donc `captain`.

Ensuite cliquez sur le bouton `unlock` et l'alerte affiche le flag.

## Write-up (english)

To reach the flag, you must enter the correct key in the form.

When we look at the source code of the page [`tresor1`](../../src/templates/tresor1.html) (right click `View Page Source`), we see a [js file](../../src/static/js/lvl1.js):
`<script src="/js/lvl1.js"></script>`.

It is possible to double click on the link `/js/lvl1.js` to access the file.

We see that to obtain the flag in an alert (`alert(data['flag'])`), you must write the correct key value in the form (`document.getElementById('key').value` ) respecting the condition `if (key === "captain")`.

The key to write in the form is therefore `captain`.

Then click on the `unlock` button and the alert displays the flag.

## Flag

`flag-C4PT41N-H3R3`
