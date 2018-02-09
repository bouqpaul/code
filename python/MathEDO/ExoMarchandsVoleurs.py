#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

plt.close('all')
a, b, c, d = 2, 1/20, 1, 1/10000

g, l = 9.81, 10

m0, v0 = 10000, 3

def evolution(t, y, a, b, c, d):
    res = np.array([y[0] * (a - b * y[1]), -y[1] * (c - d * y[0])])
    return res

def pendulePesant(t, y, g, l):
    res = np.array([y[1], g * sp.sin(y[0]) / l])
    
    return res

def euler(t0, tmax, h, y0, f, *args):  # version multidimensionnelle
    t = np.arange(t0, tmax, h)
    y = np.zeros((len(y0), len(t)))
    y[:,0] = y0
    for i in range(1, len(t)):
        y[:,i] = y[:,i-1] + h*f(t[i-1], y[:,i-1], *args)
    
    plt.plot(y[0,:], y[1,:], "b+")
    return y

def rungeKutta2(t0, tmax, h, L, y0, f, *args):
    t = np.arange(t0, tmax, h)
    y = np.zeros((len(y0), len(t)))
    c1 = 1 - (1/(2 * L))
    c2 = 1/(2 * L)
    y[:,0] = y0
    for i in range(1, len(t)):
        tk = t[i-1]
        yk = y[:,i-1]
        ff = f(tk, yk, *args)
        y[:,i] = yk + h * (c1 * ff + c2 * f(tk + L * h, yk + L * h * ff, *args))
    return y

def rungeKutta3(t0, tmax, h, y0, f, *args):
    t = np.arange(t0, tmax, h)
    y = np.zeros((len(y0), len(t)))
    y[:,0] = y0
    for i in range(1, len(t)):
        tk = t[i-1]
        yk = y[:,i-1]
        
        k1 = f(tk, yk, *args)
        k2 = f(tk + (h / 3), yk + (h * k1) / 3, *args)
        k3 = f(tk + (2 * h) / 3, yk + (2 * h * k2) / 3, *args)
        
        y[:,i] = y[:,i-1] + (h / 4) * (k1 + 3 * k3)
    
    plt.plot(y[0,:], y[1,:], "b+", mew=0.5, ms=5)
    return y

y0 = np.array([m0, v0])
#Y = rungeKutta3(0, 15, 10**(-3), y0, evolution, a, b, c, d)
#y0 = np.array([0, 20])
##################################
tmax = 1.55952*10**(9)
h = 10**(-3)
blabla = sp.integrate.ode(evolution).set_integrator("dopri5")
blabla.set_initial_value(y0, 0).set_f_params(a, b, c, d)
#V = []
#M = []
while blabla.successful() and blabla.t < tmax:
    blabla.integrate(blabla.t + h)
#    M.append(blabla.y[0])
#    V.append(blabla.y[1])
    
print(blabla.y4)
#plt.plot(M, V, "b+", mew=0.5, ms=5)

#Y = euler(0, 20, 10**(-5), y0, evolution, a, b, c, d)
#Lambda = [1/2, 2/3, 1, 2]
#
#for l, j in zip(Lambda, range(1, 5)):
#    fig = plt.figure("Runge-Kutta")
#    ax = fig.add_subplot(2, 2, j)
#    Y = rungeKutta2(0, 15, 10**(-3), l, y0, evolution, a, b, c, d)
#    ax.title.set_text("Lambda = {}".format(l))
#    ax.plot(Y[0,:], Y[1,:], "b.", linewidth=0.5)
##        plt.plot(
#plt.show()
