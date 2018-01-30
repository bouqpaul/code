#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:10:01 2017

@author: bouquepa
"""

import numpy as np
import matplotlib.pyplot as plt

NBR_POINTS = 1500
epsilon = 100
X = np.array([i for i in range(9)])
Y = np.array([0, 1.8, 19, 75, 200, 428, 796, 1344, 2117])

def normeInf(vector):
    vector = abs(np.array(vector).flatten())
    maxi = vector[0]
    for elt in vector:
        if elt > maxi:
            maxi = elt
    return maxi

def randInterv(mini=0, maxi=1, nbrVal=NBR_POINTS):
    return (np.random.rand(NBR_POINTS) * (maxi - mini)) + mini



def chercheSol(err=1, ecart=1, epsilon=200):
    plt.close('all')
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    line = ax.plot([], [], 'r.')[0]
    plt.show()
    
    A = randInterv()
    B = randInterv(2, 5)
    Ym = [0 for i in range(len(Y))]
    
    Atrouve = []
    Btrouve = []
    
    Amoy, AmoyOld = np.mean(A), 0
    Bmoy, BmoyOld = np.mean(B), 0
    
    diffA = abs(AmoyOld - Amoy)
    diffB = abs(BmoyOld - Bmoy)
    print(diffA > err)
    
    while diffA < err:
        print("While")
        for j in range(NBR_POINTS):
            a , b = A[j], B[j]
        
            for k in range(len(Ym)):
                Ym[k] = a * (X[k]**b)
            
            if normeInf(Ym - Y) < epsilon:
                print("Trouve: ", (a,b))
                Atrouve.append(a)
                Btrouve.append(b)
#        print("A trouve: ", Atrouve)
        line.set_data(Atrouve, Btrouve)
        fig.canvas.draw()
        plt.pause(0.01)
        
        AmoyOld, Amoy = Amoy, np.mean(Atrouve)
        BmoyOld, Bmoy = Bmoy, np.mean(Btrouve)
        
        A = randInterv(Amoy - ecart, Amoy + ecart)
        B = randInterv(Bmoy - ecart, Bmoy + ecart)

def chercheSolRecuit(err=0.01):
    plt.close('all')
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    line = ax.plot([], [], 'r.')[0]
    plt.show()
    
    a, b = 2, 3
    
    da, db = (2*np.random.rand())-1, (2*np.random.rand())-1
    
    YmNew = [0 for i in range(9)]
    YmOld = [0 for i in range(9)]
    
    for k in range(len(Ym):
        YmNew[k] = a * (X[k]**b)
    
    normeInf(YmNew - YmOld)
    
    
    
    

chercheSol()