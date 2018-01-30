#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ouvrir():
    try:
        chemin = input("Indiquez un chemin.\n")
        f = open(chemin, "r")
        print("Le fichier situé au '{}' a été ouvert.".format(chemin))
        double(f)        
        return f
    except IOError as err:
        print("Chemin incorrect.")
    finally:
        f.close()
        print("Done.")

def double(f):
    mot_double = []
    for line in f.readlines():
        line = line.strip("\n")
        temp = line.split(" ")
        for mot in temp:
            if estDouble(mot):
                mot_double.append(mot)
                print("Le mot '{}' est un mot 'double'.".format(mot))
                
def estDouble(mot):
    for k in range(len(mot)-1):
        if mot[k] == mot[k+1]:
            return True

def ecrireDouble(): pass
        
ouvrir()
