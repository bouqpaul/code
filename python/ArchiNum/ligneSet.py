#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from block import Block


class LigneSet(object):
    
    def __init__(self, *args, tag=1):
        self.valid = "{:01b}".format(0)
        self.tag = ("{:0" + str(tag) + "b}").format(0)
        self.block = Block(*args)
    
    
    def lire(self, blkOffset):
        return self.block.data[blkOffset:]
    
    def __str__(self):
        return "{} | {} | {}".format(self.valid, self.tag, self.block)
    

if __name__ == "__main__":
    L = LigneSet(32, tag=1)
    
    print(L)