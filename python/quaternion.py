# -*- coding: utf-8 -*-
import numpy as np
import math

def expoMat(mat, err=0.001):
    calcul = True
    n = 0
    cal_new = 0
    cal_old = 0
    while calcul:
        (cal_old, cal_new) = (cal_new, cal_new + (np.linalg.matrix_power(mat, n))/math.factorial(n))
        n += 1
        temp = cal_old - cal_new
        if MatOK(temp, err):
            calcul = False
    return cal_new

def MatOK(mat, err):
    taille = len(mat)
    for i in range(taille):
        for j in range(taille):
            if abs(mat[i,j]) > err:
                return False
    return True

M = np.array([[1,0,1],[1,0,1],[1,0,1]])
exp = expoMat(M)
print(exp)

def eulermat(phi, theta, psi):
    Aphi = phi*np.array([[0,0,0],[0,0,-1,],[0,1,0]])
    Atheta = theta*np.array([[0,0,1],[0,0,0],[-1,0,0]])
    Apsi = psi*np.array([[0,-1,0],[1,0,0],[0,0,0]])
    
    Aphi = expoMat(Aphi)
    Apsi = expoMat(Apsi)
    Atheta = expoMat(Atheta)
#    R = (Apsi.dot(Atheta)).dot(Aphi)
    R = Apsi.dot(Atheta.dot(Aphi))
    return R

print(eulermat(1,0,0))
    