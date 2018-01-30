#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *

plt.close("all")
fig = plt.figure("BlindWalker")
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim([-1, 12])
ax.set_ylim([0.5, 1.5])

xhat = array([[0],
              [1]
              ])
    
Gx = diag([0, 0.02 ** 2])
Galpha = diag([0, 0.01 ** 2])
draw_ellipse(xhat, Gx, 0.9, ax, "blue")

ex1 = zeros((20, 1))
deter = zeros((20, 1))

y = array([[1],[1]]) * 0.001
Gbeta = eye(2)* 0.001
C = eye(2) * 0.001

for k in range(19):
    if k < 10:
        u = 1
        
    else:
        u = -1
        
    Ak = array([[1, u],
                [0, 1]
                ])
    
    xhat, Gx = kalman(xhat, Gx, 0, y, Galpha, Gbeta, Ak, C)
    
    draw_ellipse(xhat, Gx, 0.99, ax, "black")
    plt.pause(0.01)
    ex1[k + 1] = sqrt(Gx[0, 0])
    deter[k + 1] = det(Gx)
    
fig = plt.figure("Ex et Deter")
ax = fig.add_subplot(2, 1, 1)
ax.plot(ex1, "red")

ax = fig.add_subplot(2, 1, 2)
ax.plot(deter, "green")

plt.show()
