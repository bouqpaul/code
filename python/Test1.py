#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import copy
import numpy as np

NBR_FRAME = 100
INTERVAL = 20

def dessin(lstMat, *args, nom="Dessin"):
    plt.close()
    
    fig = plt.figure(nom)
    
    ax = Axes3D(fig)

    
    for mat in lstMat:
        X = mat[0]
        Y = mat[1]
        Z = mat[2]
        plt.plot(X, Y, Z)
        
        if "ombre" in args:
            Zombre = [-10 for i in range(len(Z))]
            plt.plot(X, Y, Zombre, 'k')

    plt.show()

def dessinAnim(mat, *args):
    plt.close()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d', aspect='equal')
    
    ax.set_xlim3d([-5, 5])
    ax.set_ylim3d([-5, 5])
    ax.set_zlim3d([-5, 5])
    
    ax.view_init(20, 120)
    line = ax.plot([],[],[])[0]
    
    def init():
        X = mat[0]
        Y = mat[1]
        Z = mat[2]
        line.set_data(X, Y)
        line.set_3d_properties(Z)
        return line,
        
    def animate(i, args):
        global X, Y, Z
        
        if "X" in args:
            X = X + 0.2*np.cos(i/(2*np.pi))
            
        elif "Y" in args:
            Y = Y + 0.2*np.cos(i/(2*np.pi))
            
        elif "Z" in args:
            Z = Z + 0.2*np.cos(i/(2*np.pi))
            
        else:
            if "phi" in args:
                matRot = rota(mat, phi=2*i*np.pi/NBR_FRAME)
        
            elif "psi" in args:
                matRot = rota(mat, psi=2*i*np.pi/NBR_FRAME)
                
            elif "theta" in args:
                matRot = rota(mat, theta=2*i*np.pi/NBR_FRAME)
                
            X = matRot[0]
            Y = matRot[1]
            Z = matRot[2]
            
        
        line.set_data(X, Y)
        line.set_3d_properties(Z)
        
        fig.canvas.draw()
        return line,
    
    anim = animation.FuncAnimation(fig, animate, frames=NBR_FRAME,\
                                   fargs=(args), interval=INTERVAL,\
                                   blit=False, init_func=init)
                                   
    plt.show()
        


def trans(mat, qtt, *args):
    if "X" in args:
        indice = 0
        
    elif "Y" in args:
        indice = 1
        
    elif "Z" in args:
        indice = 2
        
    matCopy = copy.deepcopy(mat)
    
 
    for i in range(len(matCopy[indice])):
        matCopy[indice][i] += qtt
    
    return matCopy
        
def rota(mat, phi=0, theta=0, psi=0):
    Rphi = np.array([[1,0,0],
                    [0,np.cos(phi), -np.sin(phi)],
                    [0, np.sin(phi), np.cos(phi)]])
                    
    Rtheta = np.array([[np.cos(theta), 0, np.sin(theta)],
                        [0, 1, 0],
                        [-np.sin(theta), 0, np.cos(theta)]])
    
    Rpsi = np.array([[np.cos(psi), -np.sin(psi), 0],
                    [np.sin(psi), np.cos(psi), 0],
                    [0, 0, 1]])
     
    temp = Rpsi.dot(Rtheta).dot(Rphi).dot(mat[0:3])
    np.append(temp, [[1 for i in range(len(temp[0]))]], axis=0)                
    return temp

toto = np.array([
                [0, 0, 10, 0, 0, 10, 0, 0],
                [-1, 1, 0, -1, -.2, 0, 0.2, 1],
                [0,0,0,0,1,0,1,0],
                [1,1,1,1,1,1,1,1]
                ])
#dessin([toto])             
dessinAnim(toto, "psi")
  