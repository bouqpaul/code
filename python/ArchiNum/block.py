#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Block(object):
    
    def __init__(self, size):
        self.size = size
        self.data = ("{:0" + str(size) + "b}").format(0)
    
    def ecrire(self, data):
        sizeData = len(data)
        if sizeData <= self.size:
            self.data = self.data[:(self.size - sizeData)] + data
        else:
            self.data = data[-self.size:]
            pass
    
    def __str__(self):
        string = " ".join(list(self.data))
        return string
    
if __name__ == "__main__":
    B = Block(16)
    print(B)
    B.ecrire("12345678987654321")
    print(B)
