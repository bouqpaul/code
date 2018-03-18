#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from block import Block


class LigneSet(object):
    
    def __init__(self, *args, tag=1):
        """
        Initialisation.
        
        Une ligne contient : 
            - un bit de validité
            - tag bits pour le tag
            - un block de taille défini dans args
        """
        self.valid = "{:01b}".format(0)
        self.tag = ("{:0" + str(tag) + "b}").format(0)
        self.block = Block(*args)
    
    
    def lire(self, blkOffset):
        """
        Renvoie les bits contenu dans le block à partir du block offset.
        """
        return self.block.data[blkOffset:]
    
    def __str__(self):
        """
        Permet un affichage lisible de la ligne.
        """
        return "{} | {} | {}".format(self.valid, self.tag, self.block)
