# -*- coding: utf-8 -*-
from ASM import parser, writer
from ISS import calcPerf
import Fonctions as ff

if __name__ == "__main__":
    # Définissez le chemin du fichier contenant vos instructions
    pathFichierInstructions = "syra.txt"
    # Et le chemin du fichier pour stocker les instructions sous le langage machine
    pathFichierWriter = "binaire.txt"
    
    parse = parser(pathFichierInstructions)
    writer(pathFichierWriter, parse)
    
    # Nombre d'exécution sur lequel sera fait la moyenne des performances
    NBR_EXEC = 1000
    print("PERF MOY  : ", calcPerf(pathFichierWriter, ff.running, ff.pc, NBR_EXEC))