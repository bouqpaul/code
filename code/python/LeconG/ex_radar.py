#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *

def g(x, a, b):
    temp = np.vstack((x[0], x[2]))
    y = array([[norm(temp - a)**2],
                [norm(temp - b)**2]
                ])
    return y

def radar():
    plt.close("all")
    fig = plt.figure("Radar")
    ax = fig.add_subplot(1, 1, 1)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.show()
    
    dt = 0.01
    x = array([[4],
               [1],
               [10],
               [0]
               ])
    
    Ak = array([[1, dt, 0, 0],
                [0, 1 - 0.01 * dt, 0, 0],
                [0, 0, 1, dt],
                [0, 0, 0, 1 - 0.01 * dt]
                ])
    
    a = array([[0],
               [0]
               ])
    
    b = array([[10],
               [0]
               ])
    
    Galpha = diag([0, dt, 0, dt])
    Gbeta = 25 * eye(2)
    xhat = array([[0],
                  [0],
                  [-6],
                  [0]
                  ])
    Gx = 1000 * eye(4)
    
    for i in arange(0, 1, dt):
        plt.cla()
        plt.xlim([-10, 15])
        plt.ylim([-20, 20])
        
        plt.plot(a[0][0], a[1][0], "ob")
        plt.plot(b[0][0], b[1][0], "og")
        
        plt.plot(x[0][0], x[2][0], "+r")
        
        beta = mvnrnd2([0, 0], Gbeta)
        y = g(x, a, b) + beta
        
        draw_disk(a, sqrt(abs(y[0][0])), ax, "b")
        draw_disk(b, sqrt(abs(y[1][0])), ax, "g")
        
        temp = array([0, 0, 0, 0])
        alpha = mvnrnd2(temp, Galpha)
        
        Ck = 2 * array([[(xhat[0] - a[0])[0], 0, (xhat[2] - a[1])[0], 0],
                       [(xhat[0] - b[0])[0], 0, (xhat[2] - b[1])[0], 0]
                       ])
        
        z = y - g(xhat, a, b) + Ck @ xhat
        
        xhat, Gx = kalman(xhat, Gx, 0, z, Galpha, Gbeta, Ak, Ck)
        draw_ellipse(xhat[0:3:2], Gx[0:3:2, 0:3:2], 0.99, ax, "k")
        
        x = Ak @ x + alpha
        plt.pause(0.01)

radar()