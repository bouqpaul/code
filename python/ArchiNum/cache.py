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