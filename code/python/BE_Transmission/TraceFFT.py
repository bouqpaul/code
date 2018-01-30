#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.fftpack import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

def init():
    plt.close("all")

def TraceFFT(Fs, x, nom="TraceFFT"):
    N = len(x)
    f = np.arange(-Fs/2, (Fs/2) - (1/N), Fs/N)
    X_TFD = fft(x)
    freq = fftfreq(N) * Fs
    
    fig = plt.figure(nom)
    ax = fig.add_subplot(1, 1, 1)
    
    X = np.arange(0, Fs - (1 / N), Fs / N)
    Y = abs(X_TFD)
    ax.set_xlim(-Fs / 2, Fs / 2)
    ax.plot(freq, Y, "k")
    plt.show()

#Fs = 1000
#Freq = 100
#
#t = np.linspace(0, 2, 2 * Fs, endpoint=False)
#x = np.sin(Freq * 2 * np.pi * t)
#   
#TraceFFT(Fs, x)