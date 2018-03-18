---
title: README_BOUQUET_CLAVIER
output: pdf_document
---

# Architecture numérique et compilation

Une brève introduction s'impose, tirée du [moodle de l'ENSTA] :

*Cette partie du cours vise à la découverte de l'architecture des processeurs, au travers de la programmation d'un simulateur de jeu d'instruction d'un processeur 32 bits. Ce simulateur (ou ISS : instruction set simulator en anglais) permet de comprendre l'essence des jeux d'instructions et de la programmation assembleur. On y adjoindra un cache (ici de données).*

## Comment utiliser notre ISS ?
Utilisez le fichier main.py pour changer le chemin du fichier d'instruction et l'endroit pour sauvegarder les instructions machines.  
Vous pouvez trouver l'ensemble des fonctions disponible de l'ISS dans le fichier Fonctions.py.  
Nous avons essayé de reproduire le plus fidèlement possible le langage assembleur.  
Un calcul moyen de performance sera effectué. Par défaut, la moyenne est faite sur 1000 tests.

## Comment notre ISS fonctionne-t-il ?

Tout d'abord un parser vient lire le fichier d'instruction. Il reconnait les différentes fonctions. S'il y a une erreur de frappe ou un nom de fonctions inconnues, une erreur est soulevé et la ligne avec la faute est indiquée.  
Il est possible de définir des labels grâce au caractère spécial '$'. Toute occurence sera remplacer par le numéro de ligne correspondant.  
Exemple : 
```
BRANZ R1 $END  
$END STOP
```
On vient de définir un label pour la ligne de fin du programme et on l'utilise à tout moment dans le programme.  
Une fois qu'on a reconnu les instructions contenu dans le fichier, on les traduit en langage machine, c'est-à-dire sous forme de nombre hexadécimal selon [ce schéma] (slide 7).  
Ces instructions en langage machine sont ensuite stockées dans un fichier. Ce fichier est ensuite lu par notre ISS afin d'y être décodé. Les fonctions sont ensuite exécutées et un calcul de performance basique est effectué.  
Le calcul de performance compte un nombre de cycle sur une période de temps, puis on fait le rapport nombre de cycle sur le temps.  
Toutes les fonctions comptent pour un cycle sauf certaines qui comptent pour 2 cycles. En voici la liste :  
- mult
- div
- braz
- branz
- jmp
  
Un système de mémoire et de cache a été mieux en place ([notes de cours]).  
2 fonctions utilisent ce système : load et store.  
Load permet de charger une données de la mémoire vers les registres.  
Store permet de stocker une données dans la mémoire.  
Si la donnée est disponible dans le cache alors, il n'y aura pas de passage par la mémoire ce qui permet d'avoir des performances accrues, d'où l'intérêt du système.

[moodle de l'ENSTA]: https://moodle.ensta-bretagne.fr/course/index.php?categoryid=273
[ce schéma]: https://moodle.ensta-bretagne.fr/mod/resource/view.php?id=37647
[notes de cours]: https://moodle.ensta-bretagne.fr/pluginfile.php/57595/course/section/11557/caches-230217-1.pdf
