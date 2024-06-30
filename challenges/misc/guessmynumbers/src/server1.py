import random
import re
import os
import time

REGEX_VALIDATION = r"^(?:(?:0|-?[1-9]\d*),){9}(?:0|-?[1-9]\d*)$"
ERROR_FORMAT = '\nVous ne m\'avez pas écouté! Votre réponse doit être une séquence de 10 nombres séparés par des virgules, sans espaces.\nPar exemple: 1,2,3,4,5,6,7,8,9,10... Revenez quand vous aurez compris!'
ERROR_WRONG = '\nOops, cette séquence n\'est pas celle que j\'avais en tête. Meilleure chance la prochaine fois!'
ERROR_TIMEOUT = '\nZzzzzzz... Vous avez pris trop de temps.'
TIMEOUT = 10

def parse_numbers(val):
    if not re.match(REGEX_VALIDATION, val):
        return None
    return [int(x) for x in val.split(',')]

def rotate_logical_right(val):
    b = val & 1
    return (val >> 1) | (b << 31)

# Intro
print('Oyé oyé! Venez jouer à mon jeu de devinette!')
print('C\'est très simple, je vous donne une séquence de 10 nombres et vous devez me donner les 10 qui suivent selon le motif!')
print(f'Vous devez répondre avec une séquence de nombres séparés de virgules, sans espaces. Vous avez {TIMEOUT} secondes par niveau.')

# Level 1
start, step = random.randint(1, 1000), random.randint(1, 1000)
sequence = [start + step * i for i in range(20)]

print('\nCommençons avec quelque chose de simple...')
print(f'Niveau 1: {sequence[:10]}')
time_before, response = time.time(), parse_numbers(input('Que dites-vous? > '))

if time.time() - time_before >= TIMEOUT:
    print(ERROR_TIMEOUT)
    exit()

if not response or len(response) != 10:
    print(ERROR_FORMAT)
    exit()

if response != sequence[10:]:
    print(ERROR_WRONG)
    exit()

# Level 2
start, step1, step2 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
sequence = [start]
for i in range(19):
    num = sequence[-1]
    match i % 3:
        case 0:
            num += step1
        case 1:
            num -= step2
        case 2:
            num *= 10
    sequence.append(num)

print('\nBravo! La dernière séquence manquait de... variété. Celle-ci devrait être plus intéressante.')
print(f'Niveau 2: {sequence[:10]}')
time_before, response = time.time(), parse_numbers(input('Que dites-vous? > '))

if time.time() - time_before >= TIMEOUT:
    print(ERROR_TIMEOUT)
    exit()

if not response:
    print(ERROR_FORMAT)
    exit()

if response != sequence[10:]:
    print(ERROR_WRONG)
    exit()

# Level 3
start = random.getrandbits(32)
sequence = [start]
for _ in range(19):
    sequence.append(rotate_logical_right(sequence[-1]))

print('\nImpressionnant! Bon, pour cette dernière séquence, j\'espère que vous êtes un pro du binaire...')
print(f'Niveau 3: {sequence[:10]}')
time_before, response = time.time(), parse_numbers(input('Que dites-vous? > '))

if time.time() - time_before >= TIMEOUT:
    print(ERROR_TIMEOUT)
    exit()

if not response:
    print(ERROR_FORMAT)
    exit()

if response != sequence[10:]:
    print(ERROR_WRONG)
    exit()

# Win
print(f'\nIncroyable! Vous m\'avez battu... Voici votre récompense: {os.getenv("FLAG1")}')
print('Je vous aurez la prochaine fois!')