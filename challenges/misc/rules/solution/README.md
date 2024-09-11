# Règles

## Write-up

En allant sur la page des règlements, on peut y voir cette phrase.

> Une information importante se trouve dans l'en-tête de la réponse qui charge cette page.

En allant chercher l'en-tête de la page nous trouvons le flag.

```
❯ curl -sI  https://ctf.unitedctf.ca/rules | grep flag-
x-rule-flag: flag-RTFMPLZZZZZ
```

## Flag
`flag-RTFMPLZZZZZ`
