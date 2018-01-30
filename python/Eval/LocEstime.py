#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *

def dreadreckoning():

    x=array([[0],[0],[pi/3],[4],[0.3]])

    def f(x,u):        
        xdot= array([x[3]*cos(x[4])*cos(x[2]),
                     x[3]*cos(x[4])*sin(x[2]),
                     x[3]*sin(x[4])/3,
                     u[0],
                     u[1]
                     ])
        return xdot
    
    dt = 0.1   
    zhat= array([x[0],x[1],x[3]])
    Gzhat = zeros((3,3))
    Galphaz = dt* diag([0.01,0.01,0.01])
    Galphax = dt* diag([0,0,0.01,0.01,0.01])
    

    for t in arange(0,10,dt):
        cla()
        alphax = mvnrnd2(array([0,0,0,0,0]),Galphax)
        ux=array([[0],[0]])
        
        x=x+f(x,ux) * dt + alphax
        uz=array([[0],[0],[dt* ux[0]]])
        
        #y=array([[0],[0],[0]])
        #C=eye(3,3)     #sans odometre 
        #Gbeta=eye(3,3)
        
        Ak=array([[1,0,cos(x[4])*cos(x[2])],
                  [0,1,cos(x[4])*sin(x[2])],
                  [0,0,1]
                  ])
    
        y=x[3] + mvnrnd2(array([0]),0.1*eye(1))
        C= array([[0,0,1]])
        Gbeta= 0.01 #avec podometre qui mesure la vitesse 
        
        zhat,Gzhat= kalman(zhat,Gzhat,uz,y,Galphaz,Gbeta,Ak,C)
        
        draw_ellipse(zhat[0:2], Gzhat[0:2,0:2], 0.9, ax, 'r')
        draw_car(x)
        ax.set_xlim(-lim,lim)
        ax.set_ylim(-lim,lim)
        pause(0.01)
        
       
        
        

lim=100
fig=plt.figure()
ax=fig.add_subplot(111)
dreadreckoning()
