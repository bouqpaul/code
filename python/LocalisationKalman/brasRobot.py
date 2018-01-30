#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from roblib import *
import matplotlib.pyplot as plt
import scipy as sc
import copy

def draw_axis(R, fig, ax, lim=3):
    
#    if not (R is None):
#        R = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
#    Rrot = R[:-1, :-1]
    
#    plt.close('all')
#    fig = plt.figure()
#    ax = fig.add_subplot(projection='3d')
    
    ax.set_xlim3d([-lim, lim])
    ax.set_ylim3d([-lim, lim])
    ax.set_zlim3d([-lim, lim])
    
    debut = R.dot(array([0, 0, 0, 1]).reshape(4, 1))
    print("DEBUT: ", debut)

    finZ = R.dot(array([0, 0, 1, 1]).reshape(4, 1))
    print("FINZ: ", finZ)
    finY = R.dot(array([0, 1, 0, 1]).reshape(4, 1))
    finX = R.dot(array([1, 0, 0, 1]).reshape(4, 1))
    
    finZ = finZ - debut
    finY = finY - debut
    finX = finX - debut
    
    draw_arrow3D(ax, debut, finZ, col='b')
    draw_arrow3D(ax, debut, finY, col='g')
    draw_arrow3D(ax, debut, finX, col='r')
    
    plt.show()

#draw_axis()

def Transl(v):
    v = array(v)
    temp = eye(4,4)
    temp[:-1,-1] = v.reshape(3)
    return temp


def drawArm(R1, R2, e=2):
    J0 = array([[-e, 3*e, -e, -e],[-e,-e,3*e],[0,0,0,0],[1,1,1,1]])
    J1 = R1.dot(J0)
    J2 = R2.dot(J0)
    J = [J1[:,1], J2[:,1], J2[:,2], J1[:,2], J1[:,3], J2[:,3], J2[:,1], J2[:,2], J2[:,3], J1[:,3], J1[:,1]]
    plt.plot3D(J[1,:], J[2,:], J[3,:])
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')


A = eye(4,4)
Acopy = copy.deepcopy(A)
temp = Acopy.dot(Transl([1, 1, 1])).dot(Rot([1, 0, 0]))

drawArm(A, temp)
aae
draw_axis(A, fig, ax, lim=5)



draw_axis(temp, fig, ax, lim=5)
#draw_arrow3D(ax, array([[1], [1], [1], [1]]), array([[0],[0],[1],[1]]), col='yellow')

zrgeg
def Rot(w):
    A = array([[0,-w[2],w[1]], [w[2],0,-w[0]], [-w[1],w[0],0]])
    R = array([[0.0 for i in range(4)] for j in range(4)])
    temp = array(sc.linalg.expm(A))
    R[:3, :3] = temp
    R[-1,-1] = 1
    return R



draw_axis(R=iden)
iden = Transl([1, 1, 1]).dot(Rot([1, 0, 0]))
draw_axis(iden)


#toto = array([[42],[42],[42]])
#print(Rot(toto))
#print(Transl(toto))
    
    

