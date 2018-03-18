#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from errors import BadFonctionName

def nombreOuRegistre(reg):
    """
    Détermine si le mot reg désigne un registre ou une valeur immédiate
    """
    if reg[0] == "R" or reg[0] == "r":
        return (0, int(reg[1:]))

    else:
        return (1, int(reg))

def quatreTermes(liste, instructionBin):
    """
    Gère l'encodage des fonctions ayant 4 arguments.
    Par exemple, add, sub, ...
    """
    instructionBin += int(liste[1][1:]) << 22

    tup = nombreOuRegistre(liste[2])
    instructionBin += tup[0] << 21

    instructionBin += tup[1] << 5
    instructionBin += int(liste[3][1:])
    return instructionBin

def troisTermes(liste, instructionBin):
    """
    Gère l'encodage des fonctions ayant 3 arguments.
    Par exemple, jmp
    """
    if liste[0] == "JMP":
        tup = nombreOuRegistre(liste[1])
        instructionBin += tup[0] << 26
        instructionBin += tup[1] << 5
        instructionBin += int(liste[2][1:])

    else:
        instructionBin += int(liste[1][1:]) << 22
        instructionBin += int(liste[2])

    return instructionBin

def codeScall(liste, instructionBin):
    """
    Gère l'encodage de la fonction scall.
    """
    instructionBin += int(liste[1])
    return instructionBin

def codeStop(liste, instructBin):
    """
    Gère l'encodage de la fonction stop.
    """
    return instructBin

def parser(pathFichierInstructions):
    """
    Parse le fichier situé au chemin passé en argument.
    Transforme les instructions humaines en instructions machine,
    c'est-à-dire, des nombres hexadécimaux.
    """
    
    # Liste des instructions stockée sous forme de nombre hexadécimal
    resultat = []
    
    # Dictionnaire liant un label et un nombre de ligne
    label = {}
    
    with open(str(pathFichierInstructions), "r") as f:
        fichier = f.readlines()
        
        # Indice pour les lignes non vides
        # Permet d'aérer le code assembleur
        indice = 0
        
        # On lit le fichier une première fois pour trouver les labels
        for i in range(len(fichier)):
            # On récupère la ligne
            lines = fichier[i]
            
            # On récupère les mots
            temp = lines.strip("\n").split(" ")
            
            # Si la ligne n'est pas vide
            if temp[0] != "":
                
                # Si on définit un label sur la ligne courante
                if temp[0][0] == "$":
                    try:
                        # On regarde si on l'a déjà enregistré
                        label[temp[0]]
                        
                    except KeyError:
                        # On l'enregistre dans le cas contraire
                        label[temp[0]] = str(indice)
                    
                    # On enlève la chaine de caractère définissant un label
                    # Ex : "$monLabel ADD R1 R0 R2" devient "ADD R1 R0 R2"
                    fichier[i] = " ".join(temp[1:])
                
                # On compte les lignes non vides    
                indice += 1
                
            else:
                # Si la ligne est vide, on la passe
                continue

        for i in range(len(fichier)):
            lines = fichier[i]
            
            # Ligne vide, on passe
            if lines in ["\n"]:
                continue
            
            # On récupère les mots
            temp = lines.strip("\n").split(" ")

#            if temp[0] in label.keys():
#                temp = temp[1:]

            # On remplace les labels par leurs numéro de lignes correspondant
            for j in range(len(temp)):
                if temp[j] in label.keys():
                    temp[j] = label[temp[j]]
            
            # On regarde si le nom de la fonction correspond
            # avec ce qui est définit dans le switch
            try:
                funct = switch[temp[0]]
                
            except KeyError:
                raise BadFonctionName("'{}' à la ligne {}.".format(temp[0], i + 1))
            
            # Formation du nombre hexadécimal
            instructionBin = 0
            instructionBin += funct << 27

            nbrArgs = len(temp)
            # Traitement différent en fonction du nombre d'arguments
            try:
                instructionBin = instructionsDict[nbrArgs](temp, instructionBin)

            except KeyError:
                continue

            # Le nombre hexadécimal correspondant à l'instruction est rajouté à la liste
            resultat.append(hex(instructionBin))
    return resultat

def writer(pathFichierBin, resultat):
    """
    Écrit les résultat du parser dans un fichier situé au chemin passé en argument.
    """
    with open(str(pathFichierBin), "w") as f:
        for instru in resultat:
            f.write(str(instru)+"\n")

# Dictionnaire qui regroupe les fonctions par nombre d'arguments
instructionsDict = {1 : codeStop,
                    2 : codeScall,
                    3 : troisTermes,
                    4 : quatreTermes
                    }

# Dictionnaire permettant de faire la correspondance entre
# les fonctions et les instructions machines
switch = {"STOP"    : 0,
          "ADD"     : 1,
          "SUB"     : 2,
          "DIV"     : 3,
          "MULT"    : 4,
          "AND"     : 5,
          "OR"      : 6,
          "XOR"     : 7,
          "SHL"     : 8,
          "SHR"     : 9,
          "SLT"     : 10,
          "SLE"     : 11,
          "SEQ"     : 12,
          "LOAD"    : 13,
          "STORE"   : 14,
          "JMP"     : 15,
          "BRAZ"    : 16,
          "BRANZ"   : 17,
          "SCALL"   : 18
          }
