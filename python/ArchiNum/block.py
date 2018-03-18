#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Block(object):
    
    def __init__(self, size):
        """
        Initialisation.
        
        Un block contient :
            - sa taille
            - une chaine de caractère représentant un nombre en binaire.
              On initialise ce nombre à 0.
        """
        self.size = size
        self.data = ("{:0" + str(size) + "b}").format(0)
    
    def ecrire(self, data):
        """
        Permet d'écrire un nombre dans le block.
        Si le nombre possède un nombre de bit supérieur à la taille du block,
        seuls les bits de poids les plus faibles seront conservés.
        """
        sizeData = len(data)
        if sizeData <= self.size:
            self.data = self.data[:(self.size - sizeData)] + data
        else:
            self.data = data[-self.size:]
            pass
    
    def __str__(self):
        """
        Permet un affichage lisible de l'objet.
        """
        string = " ".join(list(self.data))
        return string
