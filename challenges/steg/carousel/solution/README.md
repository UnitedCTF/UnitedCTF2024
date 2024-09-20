# Carousel

## Write-up

Sachant que le mot de passe est composé seulement de lettres minuscules, les lettres manquantes peuvent être trouvées par un code qui essaye toutes les possibilités. 

Les mots de passe possibles peuvent être essayés avec StegHide pour trouver le flag.

```
steghide extract -sf image.jpg -p "xqnbcglrwmztpfo"
```


Cette commande devrait sortir `flag-G0Pl4yW1thTh3C4r0us3l`.


Voici un script permettant de tester les différentes combinaisons:

```py
import itertools
import subprocess
import multiprocessing

password_template = "xqn?c?l?wmz?pfo"

missing_chars_count = password_template.count('?')
possible_letters = 'abcdefghijklmnopqrstuvwxyz'

def test_password(combo):
    password = []
    combo_index = 0
    for char in password_template:
        if char == '?':
            password.append(combo[combo_index])
            combo_index += 1
        else:
            password.append(char)
    password = ''.join(password)

    result = subprocess.run(['steghide', 'extract', '-sf', 'image.jpg', '-p', password],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)


    if b"wrote extracted data" in result.stdout or b"wrote extracted data" in result.stderr:
        return password 
    return None

def main():
    with multiprocessing.Pool() as pool:
        for result in pool.imap(test_password, itertools.product(possible_letters, repeat=missing_chars_count)):
            if result:
                print(f"Password found: {result}")
                pool.terminate()
                break

if __name__ == '__main__':
    main()
```
