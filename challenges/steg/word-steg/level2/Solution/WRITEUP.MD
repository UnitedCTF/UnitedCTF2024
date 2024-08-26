# WordStego 2
## Write-up
### Solution (Français)
Si on utilise binwalk pour extraire les fichiers contenus dans le word, ou qu'on transforme le docx en zip, on peut trouver  word/media/krusty.png, qui n'est pas affiché dans le document. En ouvrant l'image on trouve le flag

flag:`flag-1sKrus7yR34l?`

### Solution (English)
We can use binwalk to extract the files in the document, or we can change the .docx to .zip and extract the archive. In the extracted files, there is word/media/krusty.png which is not shown in word. The picture contains the flag

flag:`flag-1sKrus7yR34l?`