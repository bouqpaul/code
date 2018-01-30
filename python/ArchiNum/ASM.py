#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def nombreOuRegistre(reg):
    if reg[0] == "R" or reg[0] == "r":
        return (0, int(reg[1:]))

    else:
        return (1, int(reg))

def quatreTermes(liste, instructionBin):
    instructionBin += int(liste[1][1:]) << 22

    tup = nombreOuRegistre(liste[2])
    instructionBin += tup[0] << 21

    instructionBin += tup[1] << 5
    instructionBin += int(liste[3][1:])
    return instructionBin

def troisTermes(liste, instructionBin):
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
    instructionBin += int(liste[1])
    return instructionBin

def codeStop(liste, instructBin):
    return instructBin

instructionsDict = {1:codeStop,
                    2:codeScall,
                    3:troisTermes,
                    4:quatreTermes
                    }

def parser(pathFichierInstructions):
    resultat = []
    label = {}
    with open(str(pathFichierInstructions), "r") as f:
        fichier = f.readlines()
        indice = 0
        for i in range(len(fichier)):
            lines = fichier[i]
            temp = lines.strip("\n").split(" ")
#            print("TEMP1  : ", temp)
            if temp[0] != "":
                if temp[0][0] == "$":
                    try:
                        label[temp[0]]
                    except KeyError:
                        label[temp[0]] = str(indice)
                    fichier[i] = " ".join(temp[1:])
                indice += 1
            else:
                continue


#        for i in range(len(fichier)):
#            lines = fichier[i]
#            temp = lines.strip("\n").split(" ")
#            print("EE : ", temp)
#            for i in range(len(temp)):
#                try:
#                    label[temp[i]]
#                    temp[i] = label[temp[i]]
#                except KeyError:
##                    continue
#        print("LABEL : ", label)
#        print("EREFR : ", fichier)


#        for j in range(len(fichier)):try:

#            lines = fichier[j]
##            print("LL ", lines, " J = ", j)
#            temp = lines.strip("\n").split(" ")
#            if lines in ["\n"]:
#                continue
##            print("TEMP : ", temp[0])
#            for elt in temp:
#                if elt[0] == "$":
#                    try:
#                        label[elt]
#                    except KeyError:
#                        label[elt] = str(j)
#        print("LABEL : ", label)
#        print("FICHIER : ", fichier)
        for i in range(len(fichier)):
            lines = fichier[i]
#            print("LINES : ", lines)
            if lines in ["\n"]:
                continue

            temp = lines.strip("\n").split(" ")

            if temp[0] in label.keys():
                temp = temp[1:]

            for i in range(len(temp)):
                if temp[i] in label.keys():
                    temp[i] = label[temp[i]]

#            print("FUNCT : ", temp)
            funct = switch[temp[0]]
            instructionBin = 0
            instructionBin += funct << 27

            nbrArgs = len(temp)
#            print(temp)
            try:
                instructionBin = instructionsDict[nbrArgs](temp, instructionBin)

            except KeyError:
                continue

            resultat.append(hex(instructionBin))
    print(label)
    return resultat

def writer(pathFichierBin, resultat):
    with open(str(pathFichierBin), "w") as f:
        for instru in resultat:
            f.write(str(instru)+"\n")

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

pathFichierInstructions = "instructions.txt"
parse = parser(pathFichierInstructions)
writer("binaire.txt", parse)