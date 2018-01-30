#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.io import wavfile
from TraceFFT import *
from TraceTI import *
import numpy as np
from subprocess import call

def ecoute(path):
    print("Vous êtes en train d'écouter le fichier : " + path)
    call(["mpv", path])

def dec2Bin(num):
#    print(num)
    string = list("{0:b}".format(int(num)))
    
    if string[0] == "-":
        string[0] = "0"
    else:
        string.insert(0, "1")
        
    return "".join(string)

def Sound2Bin(path):
    try:
        ecoute(path)
    except KeyboardInterrupt:
        pass
    rate , audio = wavfile.read(path)
    audio = np.average(np.array(audio), axis=1) #Si non mono
#    TraceTI(rate, audio)
#    TraceFFT(rate, audio)
    audioBin = list(map(dec2Bin, audio))
    return (rate, len(audio), audioBin)

#init()
#rate, duree, audioBin = Sound2Bin("./Data/Nightingale-sound.wav")