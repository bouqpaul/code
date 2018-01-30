#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from roblib import *
import numpy as np

fig=plt.figure()
ax= fig.add_subplot(111)
ax.set_xlim(-200,900)
ax.set_ylim(-100,800)


def indiceTrouve(elt, lst):
    indice = 0
    while indice < len(lst):
        if lst[indice] == elt:
            return indice
        indice += 1
    return -1
#----------------------------------------------
def predict(M):
    xhat=array([[0],[0],[0]])
    Gx=diag([0,0,0])
    Galpha= 0.01*eye(3,3)
    A=eye(3,3)
    for k in range(len(M)):
        #cla() #si non sacadé
        ax.set_xlim(-10,10)
        ax.set_ylim(-10,10)
        tmp = vr[k,:].reshape(3,1)
        uk = dt * eulermat(phi[k],theta[k],psi[k]) @ tmp
        xhat,Gx = kalman(xhat,Gx,uk,eye(0,1),Galpha,eye(0,0),A,eye(0,3))
        draw(k,xhat,Gx)
        pause(0.01)
#------------------------------------------------
def draw(k,xhat,Gx):
    if (k % 300) == 0:
        tmp = array([xhat[0], xhat[1]])
        draw_ellipse(tmp, Gx[0:2, 0:2], 0.9, ax, 'b')
        for i in range(3,len(xhat)-1,2):
            tmp1 = array([xhat[i], xhat[i+1]])
            draw_ellipse(tmp1, Gx[i:i+2, i:i+2], 0.9, ax, 'r')
        plt.pause(0.01)

#------------------------------------------------
def observation(depth,k,T):
    y = depth[k]
    C= zeros((1,nx))
    C[0,2]=1
    Gbeta= 0.01
    j = -1
    
#    if k in T[0]:
#        j = T[0].index(k)
#        T[0][j] = -1
        
    j = indiceTrouve(k, T[0, :])
    if j != -1:
        r = T[2][j]
        Rk = eulermat(phi[k],theta[k],psi[k])
        e = Rk @ array([[0, sqrt(r**2-(alt[k]**2)) , -alt[k]]]).T
        y=vstack((e[0:2],y))
        jm= 3+2*T[1][j]
        jm = int(jm)
        C= vstack((zeros((2,nx)),C))
        C[0,0]=1
        C[0,jm]=-1
        C[1,1]=1
        C[1,jm+1]=-1
        Gbeta= diag([1,1,0.1])
        
    return (y,C,Gbeta)

#-------------------------------------------------
def FiltreK(M,T):
    depth=M[:,7]
    xhat=zeros((nx,1))
    Ghat=diag((0,0,0, 10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5))
    Galpha = diag((0.01,0.01,0.01,0,0,0,0,0,0,0,0,0,0,0,0))
    A=eye(nx,nx)
    for k in range(len(M)):
#        cla()
        ax.set_xlim(-200,900)
        ax.set_ylim(-100,800)
        
        tmp = vr[k,:].reshape(3,1)
        uk = dt * eulermat(phi[k],theta[k],psi[k]) @ tmp
        uk = vstack((uk, zeros((2*nm, 1))))
        y, C, Gbeta = observation(depth,k,T)
        xhat,Gx = kalman(xhat,Gx,uk,y,Galpha,Gbeta,A,C)
        draw(k,xhat,Gx)
        pause(0.001)
        
#--------------------------------------------------
def smoother(M,T):
    x_forw = []
    Gx_forw = []
    uk_forw = []
    xup_forw = []
    Gup_forw = []
    
    depth=M[:,7]
    xhat= zeros((nx,1))
    x_forw.append(xhat)
    
    Gx= diag((0,0,0, 10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5,10**5))
    Gx_forw.append(Gx)
    
    Galpha = diag((0.01,0.01,0.01,0,0,0,0,0,0,0,0,0,0,0,0))
    A=eye(nx,nx)
    
    for k in range(len(M)):
#        cla()
        tmp = vr[k].reshape(3,1)
        uk = dt * eulermat(phi[k],theta[k],psi[k]) @ tmp
        uk= vstack((uk,zeros((2*nm,1))))
        
        y, C, Gbeta = observation(depth,k,T)
        
        xhat,Gx = kalman(xhat, Gx, uk, y, Galpha, Gbeta, A, C)
        xup, Gup = kalman_correc(xhat, Gx, y, Gbeta, C)
         
        x_forw.append(xhat)
        Gx_forw.append(Gx)
        xup_forw.append(xup)
        Gup_forw.append(Gup)
        draw(k,x_forw[k],Gx_forw[k])
    
    x_back = [0 for k in range(kmax)]
    G_back = [0 for k in range(kmax)]
    x_back[-1] = xup_forw[-1]
    G_back[-1] = Gup_forw[-1] 
    
    for i in range(len(M)-1,-1,1):
        J = J = Gup_forw[k] @ A.T @ inv(G_forw[k+1])
        x_back[k] = xup_forw[k]+J@(x_back[k+1]-x_forw[k+1])
        G_back[k] = Gup_forw[k]+J@(G_back[k+1]-G_forw[k+1])
        draw(k, x_back[k], G_back[k])

#------------------------- MAIN --------------------------------    
    
with open('./slam_data.txt') as fichier:
    M = []
    for ligne in fichier:
        ln = ligne.split()
        lnum = [ float(x) for x in ln]
        M.append(lnum)
    M=array(M)
    fichier.close()
    
t=M[:,0]
phi=M[:,1]
theta=M[:,2]
psi=M[:,3 ]
vr=M[:,4:7]
depth=M[:,7]
alt=M[:,8]


dt=0.1
lim=1000

np=3
nm=6
nx=np+2*nm  #  nx=15

T=array([[10540, 10920, 13740, 17480, 30380, 36880, 40240, 48170, 51720, 52320, 52790, 56880],
             [1,     2,     1,     0,     1,     5,     4,     3,     3,     4,     5,     1    ],
             [52.42, 17.47, 54.40, 52.68, 27.73, 26.98, 37.90, 36.71, 37.37, 31.03, 33.51, 15.05]])


#predict(M)
#FiltreK(M,T)

smoother(M,T)



    
