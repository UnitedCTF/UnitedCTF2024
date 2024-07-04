# JavaReverse 2
## Write-up
### Solution (Français)
En utilisant un outil comme 7zip, nous pouvons extraire tous les fichiers de l'archive JAR. Nous pouvons ensuite utiliser un IDE comme IntelliJ ou des outils en ligne pour ouvrir nos fichiers .class et obtenir le code source. En explorant, nous découvrons que le `SerialNumberValidator`  contient le flag en texte clair dans la constante MASTER_SERIAL_NO.

Flag: `flag-D0ntPuT5ecr3ts1nC0d3`

### Solution (English)

Using a tool like 7zip, we can extract all the files from the JAR archive. We can then use an IDE like IntelliJ or online tools to open our .class files and get the source code. Upon exploration, we find that the `SerialNumberValidator` contains the flag in plain text in the constant MASTER_SERIAL_NO.

Flag: `flag-D0ntPuT5ecr3ts1nC0d3`
