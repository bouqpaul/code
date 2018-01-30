#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scipy.integrate as integrate
import scipy.optimize as opti
import matplotlib.pyplot as plt

import numpy as np

v0 = 10
w = lambda x: 0
e = lambda x: w(x) / v0

def funcTemp(Xb, B):
    X = np.arange(0, Xb, 0.01)
    f = lambda x: np.sqrt((e(x) ** 2) + B)
    Y = list(map(f, X))
    res = integrate.trapz(Y, x=X)
    return res

def trajectoire(Xb, B):
    f = lambda x: np.sqrt((e(x) ** 2) + B)
    return f

def calcInte(Xa, Ya, Xb, Yb):
    B = opti.newton(lambda x: funcTemp(Xb, x) - Yb, 0.01)
    X = np.arange(Xa, Xb, 0.01)
    traj = list(map(trajectoire(Xb, B), X))
    
    f = lambda x: ((e(x) * np.sqrt(e(x) ** 2 + B)) + np.sqrt(1 + B)) / (v0 * (1 - e(x) ** 2))
    Y = list(map(f, X))
    res = integrate.trapz(Y, x=X)
    plt.close("all")
    plt.plot(traj, X)
    return res


#print(funcTemp(100, 5))
print(calcInte(10, 10, 15, 15))
