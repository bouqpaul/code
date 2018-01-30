#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from roblib import *

def dreadreckoning1(lim=50, tempsLim=50, dt=0.1):
    

    x = array([[0],
               [0],
               [0],
               [3],
               [0.2]
               ])

    def f(x,u):        
        xdot= array([x[3] * cos(x[4]) * cos(x[2]),
                     x[3] * cos(x[4]) * sin(x[2]),
                     x[3] * sin(x[4]) / 3,
                     u[0],
                     u[1]
                     ])
        return xdot
    
    zhat = array([x[0], x[1], x[3]])
    Gzhat = zeros((3, 3))
    Galphaz = dt * diag([0.01, 0.01, 0.03])
    Galphax = dt * diag([0, 0, 0.01, 0.01, 0.03])
    

    for t in arange(0, tempsLim, dt):
        cla()
        alphax = mvnrnd2(array([0, 0, 0, 0, 0]), Galphax)
        ux = array([[0],
                    [0]
                    ])
#        Euler
#        x = x + f(x,ux) * dt + alphax
    
#        Runge-Kutta
        tempX = x + (2/3) * dt * f(x, ux)
        tempU = (2/3) * dt * ux
        x = x + dt * (0.25 * f(x, ux) + (3/4) * f(tempX, tempU)) + alphax
        
        uz = array([[0],
                    [0],
                    [dt* ux[0]]
                    ])
        
        Ak = array([[1, 0, cos(x[4]) * cos(x[2])],
                    [0, 1, cos(x[4]) * sin(x[2])],
                    [0, 0, 1]
                    ])
    
        y = x[3] + mvnrnd2(array([0]), 0.1 * eye(1))
        C = array([[0, 0, 1]])
        Gbeta = 0.01 
        zhat,Gzhat= kalman(zhat,Gzhat,uz,y,Galphaz,Gbeta,Ak,C)
        
        draw_ellipse(x[0:2], Gzhat[0:2, 0:2], 0.9, ax, 'r')
        plt.plot(x[0], x[1], "+k")
#        draw_car(x)
        ax.set_xlim(-lim,lim)
        ax.set_ylim(-lim,lim)
        pause(0.01)

def dreadreckoning2(lim=50, tempsLim=50, dt=0.01):
    

    x = array([[0],
             [0],
             [0],
             [6],
             [0.1]
             ])

    def f(x,u):        
        xdot= array([x[3] * cos(x[4]) * cos(x[2]),
                     x[3] * cos(x[4]) * sin(x[2]),
                     x[3] * sin(x[4]) / 3,
                     u[0],
                     u[1]
                     ])
        return xdot
    
    zhat = array([x[0],x[1],x[3]])
    Gzhat = zeros((3,3))
    Galphaz = dt* diag([0.02, 0.02, 0.06])
    Galphax = dt* diag([0, 0, 0.02, 0.02, 0.06])
    

    for t in arange(0, tempsLim, dt):
        cla()
        alphax = mvnrnd2(array([0,0,0,0,0]),Galphax)
        ux = array([[0],[0]])

#        Euler
#        x = x + f(x,ux) * dt + alphax
        
#        Runge-Kutta
        tempX = x + (2/3) * dt * f(x, ux)
        tempU = (2/3) * dt * ux
        x = x + dt * (0.25 * f(x, ux) + (3/4) * f(tempX, tempU)) + alphax
        
        uz = array([[0],
                    [0],
                    [dt* ux[0]]
                    ])
        
        Ak = array([[1, 0, cos(x[4]) * cos(x[2])],
                    [0, 1, cos(x[4]) * sin(x[2])],
                    [0, 0, 1]
                  ])
    
        y = x[3] + mvnrnd2(array([0]), 0.1 * eye(1))
        C = array([[0,0,1]])
        Gbeta = 0.01
        
        zhat,Gzhat= kalman(zhat,Gzhat,uz,y,Galphaz,Gbeta,Ak,C)
        
        draw_ellipse(x[0:2], Gzhat[0:2, 0:2], 0.9, ax, 'r')
        plt.plot(x[0], x[1], "+k")
#        draw_car(x)
        ax.set_xlim(-lim,lim)
        ax.set_ylim(-lim,lim)
        pause(0.01)

tempsL = 20
plt.close("all")
fig = plt.figure("Deadreckoning:A")
ax = fig.add_subplot(1, 1, 1)
plt.show()
dreadreckoning1(tempsLim=tempsL)

fig = plt.figure("Deadreckoning:B")
ax = fig.add_subplot(1, 1, 1)
plt.show()
dreadreckoning2(tempsLim=tempsL)
