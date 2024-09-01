# Fastpass 1

## Write-up (français)

1. Installer l'application et l'émulateur selon le guide
2. Remarquer qu'on a un seul marteau (ou 0) pour tuer toutes les taupes
3. Décompiler l'application avec `apktool d -f -r whackamolle.apk`(les options -f et -r sont importantes car on ne touche pas aux ressources et cela peut causer des erreurs de les omettre dans notre cas)
4. Faire des recherches sur internet pour comprendre comme retrouver le code pour un jeu fait avec Unity Engine. Au lancement de l'application, le splash "Made with Unity" nous donne cet indice. [Ce lien](https://palant.info/2021/02/18/reverse-engineering-a-unity-based-android-game/)
5. Accéder à whackamolle/assets/bin/Data/Managed/ pour y trouver toutes les .dll créées à partir du code .NET original.
6. Importer toutes ces librairies dll dans dnspy
7. En faisant une recherche globale par mot clé "hammer", on trouve une fonction Awake qui stipule le nombre de marteau initialement donnés au joueur. On peut éditer la fonction dans dnspy pour mettre un très grand nombre, puis recompiler la dll et l'exporter.
8. On remplace les dll modifiées dans whackamolle/assets/bin/Data/Managed/
9. On recompile l'application avec apktool b -f -r whackamolle -o output.apktool
10. On resigne l'application. Il faut aussi la réaligner pour pouvoir l'installer. L'application apk-signer sur le Play Store permet de le faire très facilement.
11. On réinstalle l'application modifiée, on tue toutes les taupes avec nos marteaux illimités, puis le flag s'affiche.

## Write-up (english)

1. Install the application and emulator according to the guide
2. Note that you only have one hammer (or 0) to kill all the moles.
3. Decompile the application with `apktool d -f -r whackamolle.apk`(the -f and -r options are important because we don't touch the resources and it can cause errors to omit them in our case)
4. Do some research on the internet to understand how to find the code for a game made with Unity Engine. When you launch the application, the ‘Made with Unity’ splash gives you this clue. [This link](https://palant.info/2021/02/18/reverse-engineering-a-unity-based-android-game/)
5. Go to whackamolle/assets/bin/Data/Managed/ to find all the .dlls created from the original .NET code.
6. Import all these dll libraries into dnspy.
7. A global search for the keyword ‘hammer’ finds an Awake function that specifies the number of hammers initially given to the player. You can edit the function in dnspy to set a very large number, then recompile the dll and export it.
8. Replace the modified dlls in whackamolle/assets/bin/Data/Managed/.
9. Recompile the application with apktool b -f -r whackamolle -o output.apktool
10. Re-sign the application. It also needs to be realigned before it can be installed. The apk-signer application on the Play Store makes this very easy.
11. Reinstall the modified application, kill all the moles with our unlimited hammers, and the flag is displayed.


## Flag (case insensitive)

`flag-AAAF3FkxFA`
