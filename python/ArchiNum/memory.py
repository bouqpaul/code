<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Fonctions import log

class Memory(object):
    
    def __init__(self, size=32):
        self.size = size
        self.nbrBits = log(size, 2)
#        dd = (self.size % 10) + 1
#        print("dizaine ", dd)
        self.data = {("{:0" + str(self.nbrBits) + "b}").format(i) : i % (self.size // 2) for i in range(self.size)}
    
    
    def lire(self, addr, blkSize):
        demi = blkSize // 2
        nAddr = int(addr, 2)
        
        debut = nAddr - demi
        if debut < 0:
            debut = 0
        
        fin = nAddr + demi
        if fin > self.size:
            fin = self.size
        
        keys = list(self.data.keys())[debut:fin]
        data = [str(self.data[k]) for k in keys]

        return data, self.data[addr]
        
#    def ecrit(self, addr): pass

    def __str__(self):
        string = "Memoire\n"
        for (key, val) in zip(self.data.keys(), self.data.values()):
            string += "  {} -- {}\n".format(key, val)
        return string
    
if __name__ == "__main__":
    M = Memory()
    print("lire = ", M.lire("01101", 8))
    print(M)
=======
# -*- coding: utf-8 -*-



class Memory(object):
    
    def __init__(self, size=1024, nbits_data=8):
        self.size = size
        self.nbits_data = nbits_data
        
    
    def write(self, addr, data): pass
        
        
    def read(self, addr): pass

    def burstRead(self, addr, burstSize): pass

    def checkData(self, data, nbits): pass

    def checkAddresse(self, addr, size): pass
        
        
    def createDummyContent(self): pass
        

if __name__ == "__main__":
    M = Memory(size=2048, nbits_data=65687)
    print(M.size)
    print(M.nbits_data)
    
>>>>>>> 4b996067beaab4b0c7fbb5e801f4d5db5e4be804
