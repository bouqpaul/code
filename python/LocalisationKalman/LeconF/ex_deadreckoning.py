#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *


def deadreckoning():
    plt.close("all")
    fig = plt.figure("Deadreckoning")
    ax = fig.add_subplot(1,1,1)

    
    
    def f(x, u):
        xdot = array([x[3] * cos(x[4]) * cos([3]),
                      x[3] * cos(x[4]) * sin([3]),
                      x[3] * sin(x[4]),
                      u[0],
                      u[1]
                      ])
        return xdot
    
    x = array([[0],
               [0],
               [pi / 3],
               [1],
               [0.3]
               ])
    dt = 0.01
    for t in arange(0, 1, dt):
        clf()
        ax.set_xlim([-20, 20])
        ax.set_ylim([-20, 20])
        Galpha = dt * diag([0, 0, 0.01, 0.01, 0.01])
        alpha = mvnrnd2(array([0, 0, 0, 0, 0]), Galpha)
        xdot = f(x, array([[0], [0]])) * dt
        x += xdot
        draw_car(x)
        plt.pause(0.01)
        
    plt.show()

deadreckoning()
        
