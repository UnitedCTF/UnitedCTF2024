from pwn import *
from itertools import permutations

VISITOR_COUNT = 66

r = remote('localhost', port=10001)

known_categories = [set('😀💁😉🦔😜😨'), set('🥲🦐😡📎🥸'), set('🤣👾😰👩😈')]
all_visitors = set()
parks = []

r.recvuntil(b'trouvent.\n\n')
for _ in range(100):
    visitors = set(r.recvline().decode().strip()[4:].replace(' ', ''))
    all_visitors = all_visitors | visitors
    parks.append(visitors)

print(f'All visitors: {"".join(all_visitors)}')

while sum([len(s) for s in known_categories]) < VISITOR_COUNT:
    len_before_discovery = sum([len(s) for s in known_categories])

    # calculate known category overlaps of every park
    park_categories = [{i for i, cat in enumerate(known_categories) if cat & park} for park in parks]
    # only keep parks that have two known categories
    interesting_parks = [(i, s) for i, s in enumerate(park_categories) if len(s) == 2]

    # add visitors in common categories
    for i in range(len(known_categories)):
        for (x, a), (y, b) in permutations([(j, categories) for j, categories in interesting_parks if i in categories], 2):
            if len(a & b) != 1:
                continue
            a, b = parks[x], parks[y]
            known_categories[i] |= a & b

    # remove duplicates (caused by the park that has all three categories)
    for emotion in all_visitors:
        if len([cat for cat in known_categories if emotion in cat]) > 1:
            known_categories = [cat - {emotion} for cat in known_categories]

    if sum([len(s) for s in known_categories]) == len_before_discovery:
        print("Couldn't discover visitor categories from this set of parks and known visitors.")
        exit(1)

for i, category in enumerate(known_categories):
    print(f'{i+1}: {"".join(category)}')

flag_park = [i+1 for i, park in enumerate(parks) if all([cat & park for cat in known_categories])]
r.sendline(str(flag_park[0]).encode())

for _ in range(9):
    parks = []

    r.recvuntil(b'trouvent.\n\n')
    for _ in range(100):
        visitors = set(r.recvline().decode().strip()[4:].replace(' ', ''))
        all_visitors = all_visitors | visitors
        parks.append(visitors)

    flag_park = [i+1 for i, park in enumerate(parks) if all([cat & park for cat in known_categories])]
    r.sendline(str(flag_park[0]).encode())

r.interactive()