#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def TraceTI(Fs, x, nom="TraceTI"):
    x = np.array(x)
    fig = plt.figure(nom)
    
    ax = fig.add_subplot(1, 1, 1)
    tmp = (len(x) - 1) / Fs
#    t = np.arange(0, tmp / Fs, 1 / Fs)
    t = np.linspace(0, tmp, len(x))
    
    N = len(t)
    tMax, tMin = t[-1], t[0]
    
    ax.set_xlim(tMin, tMax)
    ax.plot(t, x, "k")
    plt.show()
    
#    Module_X = abs(x)
#    ax = fig.add_subplot(1, 2, 2)
#    ax.set_xlim(tMin, tMax)
#    ax.plot(t, Module_X, "k")
    
#Fs = 1000
#Freq = 1
#
#t = np.linspace(0, 2, 2 * Fs, endpoint=False)
#x = np.sin(Freq * 2 * np.pi * t)
#   
#TraceTI(Fs, x)