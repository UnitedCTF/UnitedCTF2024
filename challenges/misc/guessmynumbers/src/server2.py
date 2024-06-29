import random
import re
import os
import socket
import time
import datetime

def parse_numbers(val):
    return [int(x) for x in val.split(',') if re.match(r"^[^0 \t\v\n\r]*[1-9]\d*$", x)]

# Intro
print('Ah, si vite de retour! J\'ai remanié le jeu depuis la dernière fois...')
print('Je vais choisir 10 nombres au pur hasard, vous devrez les deviner sans aucune information de ma part!')
print('Pour rendre les choses plus justes, vous avez accès à la logique derrière mes choix. (voir CTFd)')

# Input & validation
print(f'\nCette fois, il n\'y a qu\'un niveau, mais faites vite! Je n\'ai pas toute la journée à attendre, il est déjà {datetime.datetime.now()}')
response = input('Que dites-vous? > ')
response_sequence = parse_numbers(response)

if len(response_sequence) != 10:
    print("\nAttention! Votre séquence doit contenir 10 nombres valides. Revenez quand vous aurez compris!")
    exit()

# Generate sequence
seed = int.from_bytes(socket.gethostname().encode(), byteorder='little') # Seed with hostname bytes
seed ^= int.from_bytes(response[:16].encode(), byteorder='little')       # Throw in some entropy from the user input
seed ^= int(time.time())                                                 # Throw in the time for good measure

random.seed(seed)
sequence = [random.getrandbits(32) for _ in range(10)]

# Verify sequence
if response_sequence != sequence:
    print(f'\nEt non! La séquence que j\'avais en tête était {sequence}.')
    print('Meilleure chance la prochaine fois!')
    exit()

# Win
print(f'\nJe n\'y crois pas, vous l\'avez eue... Prenez votre récompense et ne revenez plus! {os.getenv("FLAG2")}')