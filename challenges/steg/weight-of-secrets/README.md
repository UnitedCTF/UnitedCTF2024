# Weight of Secrets

**`Auteur:`** [Hannibal119](https://github.com/armandBriere)

## Description (français)

C'est toujours la même chose avec ce Monty Leroy. Il ne cesse de parler de son "IA" et de comment cela va changer le monde. Mais vous savez, vous savez que l'IA n'est qu'un amas de nombres et de poids. Je n'arrive pas à croire qu'on travaille encore avec lui...

De toute façon, il me doit de l'argent pour la "Cartesian Glide" que nous construisons, et il m'a dit que le mot de passe de paiement se trouve quelque part dans ce fichier. Je ne sais pas de quoi il parle, mais je suis sûr que vous pouvez le trouver pour moi.

## Description (english)

It's always the same thing with that Monty Leroy guy. He's always talking about his "AI" and how it's going to change the world. But you know better. You know that AI is just a bunch of numbers and weights. I can't believe we are still working with that guy...

Anyway, he owes me some money for the "Cartesian Glide" slope we are building and he told me the payment password is in that file somewhere. I don't know what he's talking about, but I'm sure you guys can find it for me.

Flag format: flag-[0-9a-zA-Z_]{24}

## Solution

The script `main.py` that creates the model is also validating that the model contains the correct flag after creation/

Expected output:

```bash
Model created with 29 layers
Weights changed
Model saved to model.pth
Model loaded from model.pth
Flag: flag-th3_we1gh7s_4rE_7H3_fL4g
Flag is correct!
```

An detailed explanation of the solution can be found in the [solution](./solution/README.md) file.
