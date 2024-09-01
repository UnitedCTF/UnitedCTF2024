# Bateau pirate

**`Auteur.e`** [Deimos](https://github.com/amDeimos666)

## Description (français)

On vient de terminer les derniers détails avant de réouvrir le bateau pirate. Le Capitaine m'a demandé de faire une dernière inspection pour s'assurer que nos secrets restent entre bonnes mains.
Veux-tu m'aider? Ça ira plus vite!

## Description (english)

We just finished the last details before reopening the pirate ship. The Captain asked me to do a final inspection to make sure our secrets stay in good hands.
Will you help me? It'll go faster!

## Challenges

### Nettoyage

Challenge can be found [here](./nettoyage/README.md).

### Citation

Challenge can be found [here](./citation/README.md).

### Peinture

Challenge can be found [here](./peinture/README.md).

### Secret

Challenge can be found [here](./secret/README.md).

### Tresor 1

Challenge can be found [here](./tresor1/README.md).

### Tresor 2

Challenge can be found [here](./tresor2/README.md).

## Setup

The challenge will be locally hosted at <http://localhost:10500>

### Local

```bash
cd ./challenges/web/bateau-pirate/src/
pip install flask
FLASK_APP=src/app.py FLASK_ENV=development
flask run --port 10500
```

### Docker

```bash
cd ./challenges/web/bateau-pirate/
docker build -t bateau-pirate .
docker run -p 10500:5000 bateau-pirate
```
