#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def diffusion(t, thetaA=25, thetaE=1800, L=5*10**(-2), x=2.5*10**(-2), n=100, a=33*10**(-8)):
    A = 0
    coeff = 4 * (thetaA - thetaE)/np.pi
    for i in range(n):
        indice = 2 * i + 1
        s = np.pi * x * (indice) / L
        e = (-((indice) * np.pi / L)**2) * a * t
        Ai = coeff * (1 / (indice)) * np.sin(s) * np.exp(e)
        A += Ai

    A += thetaE
    return A

def theta(objectif=1410, err=1, pas=5, t=0):
    plt.close("all")
    plt.figure("Température")
    
    temperature = diffusion(t)
    
    Y = [temperature]
    X = [t]
    while abs(objectif - temperature) > err:
        t += pas
        X.append(t)
        temperature = diffusion(t)
        Y.append(temperature)
    
    plt.plot(X, Y, "red")
    return t

resultat = theta()
print(resultat)
    
    