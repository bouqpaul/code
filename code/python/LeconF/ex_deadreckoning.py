#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *


def deadreckoning():
    plt.close("all")
    fig = plt.figure("Deadreckoning")
    ax = fig.add_subplot(1,1,1)

    
    
    def f(x, u):
        xdot = array([x[3] * cos(x[4]) * cos([2]),
                      x[3] * cos(x[4]) * sin([2]),
                      x[3] * sin(x[4]),
                      u[0],
                      u[1]
                      ])
        return xdot
    
    x = array([[0],
               [0],
               [pi / 3],
               [4],
               [0.3]
               ])
    dt = 0.01
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    
    zhat = array([x[0],
                  x[1],
                  x[3]
                  ])
    
    Gz = zeros((3, 3))
    Galphax = dt * diag([0, 0, 0.01, 0.01, 0.01])
    Galphaz = dt * diag([0.01, 0.01, 0.01])    
    
    for t in arange(0, 1, dt):
        plt.cla()
        
        alphax = mvnrnd2(array([0, 0, 0, 0, 0]), Galphax)
        ux = array([[0], [0]])
        
        x = x + f(x, ux) * dt + alphax
        
        uz = array([[0],
                    [0],
                    [dt * ux[0]]
                    ])
#        Sans odomètre
    
#        y = array([[0],
#                   [0],
#                   [0]
#                   ])
#    
#        C = eye(3)
#        Gbeta = eye(3)
        
    
#        Lock
        y = x[3] + mvnrnd2([0], [[0.1]])
        C = array([[0, 0, 1]])
        Gbeta = 0.1
        
        Ak = array([[1, 0, dt * cos(x[4]) * cos(x[2])],
                    [0, 1, dt * cos(x[4]) * sin(x[2])],
                    [0, 0, 1]
                    ])
    
        zhat, Gz = kalman(zhat, Gz, uz, y, Galphaz, Gbeta, Ak, C)
        draw_ellipse(zhat[0:2], Gz[0:2:1, 0:2:1], 0.9, ax, "k")
        draw_car(x)
        
        ax.set_xlim([-20, 20])
        ax.set_ylim([-20, 20])
        
        plt.pause(0.01)
        
    plt.show()

deadreckoning()
        
