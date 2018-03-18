#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ligneSet import LigneSet
from errors import BadSelection
#from Fonctions import log
from numpy import log2
from memory import Memory


class Cache(object):
    def __init__(self, S, E, B, m, memory):
        """
        Initialisation de du cache.
        Le cache contient : 
            - S sets
            - E nombre de ligne par set
            - B bits par block
            - m nombre d'adresse
            - memory, une mémoire qui est lié au cache
        """
        self.nbrSet = S
        self.nbrLine = E
        self.blkSize = B
        self.addrBits = m
        
        # Calcul de la taille
        self.size = B * E * S
        
        # Calcul du nombre de bits de sélection
        self.s = int(log2(S))
        # Calcul de l'offset pour la lecture du block
        self.b = int(log2(B))
        # Calcul du nombre de bits de tag
        self.t = m - (self.s + self.b)
        
        self.memory = memory
        
        # Ensemble des sets du cache.
        # Un set est composé de une ou plusieurs "ligne"
        # Chaque ligne contient un bit de validité, t bits de tag et un block de B bits
        self.sets = {("{:0" + str(self.s) + "b}").format(i) : [LigneSet(B, tag=self.t) for j in range(E)] for i in range(self.nbrSet)}
        
        # Dictionnaire permettant de connaitre quelle ligne de quel set à été utilisé en dernier
        # Ce dictionnaire permet de réallouer de la mémoire selon l'algorithme du Least Recently Used
        self.lru = {("{:0" + str(self.s) + "b}").format(i) : [j for j in range(E)] for i in range(self.nbrSet)}
    
    
    def updateLRU(self, selectBits, selectedLgn):
        """
        Rafraichit l'ordre des lignes récemment utilisées.
        selectedLgn devient la ligne la plus récemment utilisée.
        """
        
        # On récupère l'indice de la ligne sélectionnée dans
        # l'ensemble des lignes du set défini par selectBits
        indice = self.sets[selectBits].index(selectedLgn)
        
        # On récupère l'ensemble des lignes pour le set selectBits
        temp = self.lru[selectBits]
        
        # On insère l'indice de la ligne à la fin de la liste
        temp.insert(len(temp), indice)
        
        # On enlève la première occurrence de l'indice dans la liste
        # De cette manière, la ligne qui a été la plus récemment utilisées
        # ce trouve en fin de liste.
        # La ligne qui a été utilisée le moins souvent se trouve en début de liste.
        temp.remove(indice)
        
        # On rafraichit la liste avec les nouvelles positions
        self.lru[selectBits] = temp

    def ecrit(self, addr, selectedLgn, tagBits, selectBits):
        """
        Permet d'écrire dans le cache à l'adresse addr.
        """
        
        # On récupère la valeur dans la mémoire
        data, valeur = self.memory.lire(addr, self.blkSize)
        
        # On écrit dans le block
        # On rafraichit les valeurs de tag et validité
        selectedLgn.block.ecrire("".join(data))
        selectedLgn.tag = tagBits
        selectedLgn.valid = "1"
        
        # On rafraichit la dernière ligne utilisée
        self.updateLRU(selectBits, selectedLgn)

        return valeur
        
    def champsBits(self, addr):
        """
        Renvoie les bits de sélection, tag et block offset.
        """
        tagBits = addr[:self.t]
        selectBits = addr[self.t:(self.s + self.t)]
        blkOffset = addr[self.t + self.s:]
        
        return (tagBits, selectBits, blkOffset)
        
    def lire(self, addr):
        """
        Permet de lire dans le cache.
        Si l'adresse n'est pas chargée, lance une série de lecture dans la mémoire.
        """
        
        # On récupère les différents bits
        tagBits, selectBits, blkOffset = self.champsBits(addr)
        
        try:
            # On récupère la ligne la moins récemment utilisée
            indice = self.lru[selectBits][0]
            selectedLgn = self.sets[selectBits][indice]
            
            # Si la ligne est valide
            if int(selectedLgn.valid, 2) == 1:
                
                # Possède le bon tag
                if selectedLgn.tag == tagBits:
                    # On renvoie la valeur à partir du block offset
                    return selectedLgn.lire(int(blkOffset))
    
                else:
                    # La ligne ne possède pas le bon tag
                    # Il faut la charger dans le cache
                    return self.ecrit(addr, selectedLgn, tagBits, selectBits)
            
            else:
                # La ligne n'est pas valide (cache miss)
                # Il faut la charger dans le cache
                return self.ecrit(addr, selectedLgn, tagBits, selectBits)
        
        except KeyError:
            # Erreur dans les bits de sélection
            raise BadSelection("{}".format(selectBits))
            
    
        
    def __str__(self):
        """
        Permet un affichage de l'objet.
        """
        string = "Cache || t = {}, s = {}, b = {}\n".format(self.t, self.s, self.b)
        for (nbr, l) in zip(self.sets.keys(), self.sets.values()):
            for ligne in l:
                string += "  {} -- {}\n".format(nbr, ligne)

        return string
