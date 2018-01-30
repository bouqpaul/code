# -*- coding: utf-8 -*-
#mul = [i*7 for i in range(1, 21)]
#print(mul)
#
def conversion(euro):
    euro = int(euro)
    for i in range(euro):
        print("{} euro(s) = {:.2f} dollar(s)".format(i, i*1.65))
conversion(20)
#
#def trouve(caract, chaine):
#    cara = str(caract)
#    chaine = str(chaine)
#    nbr = chaine.count(cara)
#    if nbr:
#        print("Il y a '{}' dans '{}'".format(cara, chaine))
#    else:
#        print("Il n'y a pas '{}' dans '{}'".format(cara, chaine))
#print(trouve("e", "azdfgdfg"))
##
#trouve("e", "Monty python flying circus")

#def change(chaine):
#    chaine = list(str(chaine))
#    result = []
#    for i in range(len(chaine)-1, -1, -1):
#        result.append(chaine[i])
#        
#    return "".join(result)
#
#print(change("zorglub"))

#Jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#Mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
#      'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
#result = []
#for nbr, mois in zip(Jours, Mois):
#    result.append(mois)
#    result.append(nbr)
#print(result)
#
#def affichage(liste):
##    print("affichage : ", liste)
#    return " ".join(liste)
#print(affichage(Mois))
#
#def Max(liste):
#    maximum = liste[0]
#    for elt in liste:
#        if elt > maximum:
#            maximum = elt
#    print("Le plus grand élément de cette liste a la valeur : {}.".format(maximum))
#Max([32, 5, 12, 8, 3, 75, 2, 15])
#
#def PairImpair(liste):
#    p, i = [], []
#    for elt in liste:
#        if elt %2 == 0:
#            p.append(elt)
#        else:
#            i.append(elt)
#    return p, i
#print(PairImpair([32, 5, 12, 8, 3, 75, 2, 15]))