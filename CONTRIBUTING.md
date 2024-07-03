# Directives de contribution

## Pour commencer
- Faites un fork du répertoire pour travailler sur votre défi.

## Organisation & requis
- Les défis devraient être créés sous l'arborescence `challenges/<catégorie>/<nom du défi>`
- Chaque défi devrait contenir:
    - Un README.md avec le nom de l'auteur, une description en français et en anglais, sans oublier le flag (faites un double-check pour s'assurer qu'il est identique).
    - Un fichier `<nom du défi>.yml` contenant des détails sur le défi selon la [spécification ctfcli](https://github.com/CTFd/ctfcli/blob/master/ctfcli/spec/challenge-example.yml). Pas besoin de tout remplir, il faut seulement:
        - name
        - author
        - category
        - description (en + fr)
        - flag(s)
        - tags
        - files (si applicable)
        - hints (si applicable)
        - requirements (si le challenge suit un autre)
    - Un document similaire au README pour décrire votre solution avec des étapes. Si la solution peut être automatisée, un script de vérification automatique serait grandement apprécié.
    - Si le challenge nécessite un déploiement:
        - Un `Dockerfile` pour le défi avec une directive `EXPOSE` pour clairement identifier le port qui doit être exposé par l'infrastructure. Si le challenge nécessite plusieurs conteneurs, fournissez un `docker-compose.yml` avec les services nécessaires.
    


## Sanity checks
- Est-ce que vous avez réussi à résoudre votre propre challenge?
- Est-ce que quelqu'un qui n'a pas designé le challenge serait capable de tirer les conclusions nécessaires à la complétion du challenge?
- Est-ce que votre challenge est le fun ou intéressant? S'il nécessite beaucoup de temps, est-ce par nécessité et est-ce raisonnable?
- Est-ce que la solution de votre challenge dépend d'un langage, d'une librairie ou d'une version spécifique d'une librairie/d'un framework? Si oui, assurez-vous que ça soit indiqué explicitement _ou implicitement_.
- Si votre challenge est mutable, assurez-vous que les actions d'un joueur ne puissent pas impacter négativement un autre joueur (ou leaker la solution).
    - Dans le cas où le défi est mutable et qu'il n'est pas possible de bien isoler les actions de chaque joueur, spécifiez que votre challenge nécessite des instances individuelles au moment de la pull request.

## Au moment de la pull request...
- Créez votre pull request vers la branche `main` du répertoire principal.
- Si votre défi a des besoins particuliers (accès à l'internet, **instances individuelles par joueur**, bot discord, réseaux virtuels, etc.), veuillez les spécifier. Si vous avez des besoins _très_ particuliers, contactez `@linkster78` sur Discord pour voir si c'est faisable.
- Annoncez que votre challenge est prêt au QA dans le canal de communication `#qa` sur Discord.
- Suivez votre pull request au cas où il y aurait des choses à changer ou des questions lors du QA (cette communication peut se faire sur Discord selon vos préférences).
- Attendez que la branche soit approuvée et révisée par au moins une personne du QA ou de l'organisation avant de la pousser sur `main`.