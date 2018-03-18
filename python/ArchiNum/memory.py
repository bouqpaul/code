#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import log2

class Memory(object):
    
    def __init__(self, size=32):
        """
        Initialisation.
        La memory n'est définie que par sa taille.
        Le reste est déduit de cette information.
        """
        self.size = size
        self.nbrBits = int(log2(size))
        
        # On représente la mémoire par un dictionnaire
        # Les clés sont les adresses
        # Les valeurs sont les données stockées.
        # On les initialise à 0
        self.data = {("{:0" + str(self.nbrBits) + "b}").format(i) : i for i in range(self.size)}
    
    
    def lire(self, addr, blkSize):
        """
        Permet de lire dans la mémoire sur une longueur de blkSize centrée sur addr.
        """
        
        demi = blkSize // 2
        nAddr = int(addr, 2)
        
        # Borne inférieure
        debut = nAddr - demi
        if debut < 0:
            debut = 0
        
        # Borne supérieure
        fin = nAddr + demi
        if fin > self.size:
            fin = self.size
        
        # On récupère l'ensemble des adresses
        keys = list(self.data.keys())[debut:fin]
        
        # On récupère les valeurs stockées à ces adresses
        data = [str(self.data[k]) for k in keys]
        
        # On renvoie l'ensemble des valeurs à charger dans le cache (data)
        # et renvoie la valeur à l'adresse addr (self.data[addr])
        return data, self.data[addr]
        
    def ecrit(self, addr, nData):
        """
        Écrit nData à l'adresse addr
        """
        self.data[addr] = nData

    def __str__(self):
        """
        Permet un affichage de l'objet.
        """
        string = "Memoire\n"
        for (key, val) in zip(self.data.keys(), self.data.values()):
            string += "  {} -- {}\n".format(key, val)
        return string
