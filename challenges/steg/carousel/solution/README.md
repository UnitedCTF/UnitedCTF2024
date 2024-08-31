# Carousel

## Write-up

Sachant que le mot de passe est composé seulement de lettres minuscules, les lettres manquantes peuvent être trouvées par un code qui essaye toutes les possibilités. 

Les mots de passe possibles peuvent être essayés avec StegHide pour trouver le flag.

```
steghide extract -sf image.jpg -p "xqnbcglrwmztpfo"
```

Cette commande devrait sortir `flag-G0Pl4yW1thTh3C4r0us3l`.