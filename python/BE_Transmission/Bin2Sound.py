#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Sound2Bin import *
from TraceFFT import *
from TraceTI import *
from scipy.io import wavfile
import numpy as np

def Bin2Sound(audioBin):
    audioDecode = []
    for binaire in audioBin:
        multi = 1
        if binaire[0] == "0":
            multi = -1

        temp = multi * int(binaire[1:], 2)
        audioDecode.append(temp)
    rate = 44100
#    TraceTI(Fs, audioDecode, "TI")
#    TraceFFT(Fs, audioDecode, "FFT")
    audioDecode = np.asarray(audioDecode, dtype=np.int16)
    wavfile.write("./Data/Output.wav", rate, audioDecode)
    
    try:
        ecoute("./Data/Output.wav")
    except KeyboardInterrupt:
        pass
    
    return audioDecode
    
#init()
#(a, b, c) = Sound2Bin("./Data/Nightingale-sound.wav")
#Bin2Sound(c)