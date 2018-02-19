# -*- coding: utf-8 -*-


class Block(object):
    
    
    def __init__(self, valid, tagBits, data, size=16):
        self.valid = valid
        self.tagBits = tagBits
        self.data = data
        self.size = size
    
    def __str__(self):
        return "Je suis le block {} avec la data {}".format(self.tagBits, self.data)

