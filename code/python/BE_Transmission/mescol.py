#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
from scipy.signal import butter, lfilter
from Sound2Bin import *
from TraceFFT import *
from TraceTI import *



def passeBande(bas, haut, Fe, order=5):
    nyq = 0.5 * Fe
    tmp = [bas / nyq, haut / nyq]
    b, a = butter(order, tmp, btype='band')
    return b, a

def filtrePasseBande(data, low, high, Fe, order=5):
    b, a = passeBande(low, high, Fe, order=order)
    y = lfilter(b, a, data)
    return y

def mescol(B, Ns, maxi=10):
    messageAlea = np.random.randint(0, high=maxi, size=(Ns))
    messageAleaFiltre = filtrePasseBande(messageAlea, 1000, B, 44200)
    messageAleaFiltre = list(map(lambda x: int("{0:b}".format(int(x)), 2), messageAleaFiltre))
    return messageAleaFiltre
