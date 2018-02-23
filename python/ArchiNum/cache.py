<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ligneSet import LigneSet
from errors import BadSelection
from Fonctions import log
from memory import Memory


class Cache(object):
    def __init__(self, S, E, B, m, memory):
        self.nbrSet = S
        self.nbrLine = E
        self.blkSize = B
        self.addrBits = m
        
        self.size = B * E * S
        
        self.s = log(S, 2)
        self.b = log(B, 2)
        self.t = m - (self.s + self.b)
        
        self.memory = memory
        self.sets = {("{:0" + str(self.s) + "b}").format(i) : [LigneSet(B, tag=self.t) for j in range(E)] for i in range(self.nbrSet)}
        self.lru = {("{:0" + str(self.s) + "b}").format(i) : [j for j in range(E)] for i in range(self.nbrSet)}
    
    
    def updateLRU(self, selectBits, selectedLgn):
        indice = self.sets[selectBits].index(selectedLgn)
        
        temp = self.lru[selectBits]
        temp.insert(len(temp), indice)
        temp.remove(indice)
        self.lru[selectBits] = temp

    def ecrit(self, addr, selectedLgn, tagBits, selectBits):
        data, valeur = self.memory.lire(addr, self.blkSize)
        
        selectedLgn.block.ecrire("".join(data))
        selectedLgn.tag = tagBits
        selectedLgn.valid = "1"
        self.updateLRU(selectBits, selectedLgn)

        return valeur
        
    def champsBits(self, addr):
        tagBits = addr[:self.t]
        selectBits = addr[self.t:(self.s + self.t)]
        blkOffset = addr[self.t + self.s:]
        
        return (tagBits, selectBits, blkOffset)
        
    def lire(self, addr):
        
        tagBits, selectBits, blkOffset = self.champsBits(addr)
#        print("addr = ", addr)
#        print("tag = ", tagBits)
#        print("select = ", selectBits)
#        print("blk = ", blkOffset)
        
        try:
            indice = self.lru[selectBits][0]
            selectedLgn = self.sets[selectBits][indice]
            if int(selectedLgn.valid, 2) == 1:
                if selectedLgn.tag == tagBits:
                    return selectedLgn.lire(int(blkOffset))
    
                else:
                    return self.ecrit(addr, selectedLgn, tagBits, selectBits)
#                    raise BadTag("Adresse : {} || Ligne : {}".format(tagBits, selectedLgn.tag))
            
            else:
                return self.ecrit(addr, selectedLgn, tagBits, selectBits)
        
        except KeyError:
            raise BadSelection("{}".format(selectBits))
            
    
        
    def __str__(self):
        string = "Cache || t = {}, s = {}, b = {}\n".format(self.t, self.s, self.b)
        for (nbr, l) in zip(self.sets.keys(), self.sets.values()):
            for ligne in l:
                string += "  {} -- {}\n".format(nbr, ligne)

        return string
    
if __name__ == "__main__":
    M = Memory(size=16)
    C = Cache(4, 1, 2, 4, M)
    print(C.memory)
    print(C)
    print("Lecture de 0101")
    print("Je lis : ", C.lire("0101"))
    print("Lecture de 0100")
    print("Je lis : ", C.lire("0100"))
    print("Lecture de 1110")
    print("Je lis : ", C.lire("1010"))
    print(C)
    
=======
# -*- coding: utf-8 -*-


from block import Block

class Cache(object):
    
    def __init__(self, memory, nbSets=4, blocSize=2):
        self.memory = memory
        self.sets = [Block(0, i, "d") for i in range(nbSets)]
        self.nbSets = nbSets
        self.blocSize = blocSize
    
    def __str__(self):
        return str(list(map(print, C.sets)))
    
    def read(self, addr):
        for block in self.sets:
            if block.valid and block.tagBits == addr:
                return block.data
        return None
            
            

    def write(self, addr, data):
        


    def writeThrough(self, addr, data): pass
    
    def to_s(self): pass

if __name__ == "__main__":
    C = Cache([], [])
    print(C)
>>>>>>> 4b996067beaab4b0c7fbb5e801f4d5db5e4be804
