import random
import os
import time

EMOJIS = [
    list("😢🥲😥😭😰😵🤕🤬😡🤢😫🤮💀"),
    list("😀😁🤣😄😎😆😋😍🤗😏😜😌🤪"),
    list("🥸🤡👾👻📎👺🤖🙊🦐🦭🦔💅🗿")
]

EMOJIS_PER_PARK = 6
PARK_COUNT = 100
ROUND_COUNT = 10
TIMEOUT = 10

for round in range(ROUND_COUNT):
    flag_park_emojis = random.sample(EMOJIS[0], 2) + random.sample(EMOJIS[1], 2) + random.sample(EMOJIS[2], 2)
    random.shuffle(flag_park_emojis)
    flag_park_idx = random.randint(0, PARK_COUNT-1)

    parks = []

    for i in range(PARK_COUNT):
        if i == flag_park_idx:
            emotions = flag_park_emojis
        else:
            ensemble1, ensemble2 = random.sample(EMOJIS, 2)
            emotions = random.sample(ensemble1 + ensemble2, EMOJIS_PER_PARK)

        parks.append({'id': i + 1, 'emotions': emotions})

    print(f'[Ronde {round+1}/{ROUND_COUNT}] Voici la liste des parcs et les émotions qui y ont été recensées.\n')

    for park in parks:
        print(f"{str(park['id']).rjust(3, ' ')}: {' '.join(park['emotions'])}")

    time_before = time.time()
    resp = input("\nRAPPEL: On cherche le parc qui provoque des émotions des trois catégories: positives, négatives et autres.\nQuel est l'identifiant du parc en question?\n> ")
    
    if time.time() - time_before >= TIMEOUT:
        print('Vous avez pris trop de temps! Les données changent aux dix secondes...')
        exit(1)

    if resp != str(flag_park_idx+1):
        print('Mauvais parc, meilleure chance la prochaine fois!')
        exit(1)
    else:
        print('Bravo!\n')

print('Vous nous avez grandement aidé! Voici votre récompense: ' + os.getenv('FLAG1'))
