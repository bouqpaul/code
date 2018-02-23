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
    