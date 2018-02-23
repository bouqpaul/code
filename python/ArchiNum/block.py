<<<<<<< HEAD
#!/usr/bin/env python3
=======
>>>>>>> 4b996067beaab4b0c7fbb5e801f4d5db5e4be804
# -*- coding: utf-8 -*-


class Block(object):
    
<<<<<<< HEAD
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
#    ss = " ".join(list(B.data))
#    print(ss)
=======
    
    def __init__(self, valid, tagBits, data, size=16):
        self.valid = valid
        self.tagBits = tagBits
        self.data = data
        self.size = size
    
    def __str__(self):
        return "Je suis le block {} avec la data {}".format(self.tagBits, self.data)

>>>>>>> 4b996067beaab4b0c7fbb5e801f4d5db5e4be804
