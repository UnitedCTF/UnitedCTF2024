# Gimme privileges (Krusty Bot)

## Write-up (français)

Comme indiqué par la description, les ballons sont stockés dans une base de données.
On peut alors essayer de faire une injection SQL pour récupérer le ballon spécial.

En utilisant la commande `/balloon_buy` avec l'argument `' OR 1=1 --`, on peut récupérer le ballon spécial.
Le flag est affiché directement dans le message de réponse.

## Write-up (english)

As indicated by the description, the balloons are stored in a database.
We can then try to do an SQL injection to retrieve the special balloon.

By using the command `/balloon_buy` with the argument `' OR 1=1 --`, we can retrieve the special balloon.
The flag is displayed directly in the response message.
