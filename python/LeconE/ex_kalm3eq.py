#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *


plt.close("all")
plt.ion()
fig = plt.figure("Kalman 3 equations")
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

Galphas = zeros(2)
A = eye(2)

C0 = array([[2, 3]])
C1 = array([[3, 2]])
C2 = array([[1, -1]])

y0 = 8
u = 0
xhat0 = array([[0],[0]])
Gx0 = 1000 * eye(2)
draw_ellipse(xhat0, Gx0, 0.9, ax, "red")

xhat1, Gx1 = kalman(xhat0, Gx0, u, 8, Galphas, 1, A, C0)
draw_ellipse(xhat1, Gx1, 0.9, ax, "blue")

xhat2, Gx2 = kalman(xhat1, Gx1, u, 7, Galphas, 4, A, C1)
draw_ellipse(xhat2, Gx2, 0.9, ax, "magenta")

xhat3, Gx3 = kalman(xhat2, Gx2, u, 0, Galphas, 4, A, C2)
draw_ellipse(xhat3, Gx3, 0.9, ax, "black")


y = array([[8], [7], [0]])
Gbeta = diag([1, 4, 4])
C = np.row_stack((C0, C1, C2))
xhat, Gx = kalman(xhat0, Gx0, u, y, Galphas, Gbeta, A, C)
draw_ellipse(xhat, Gx, 0.9, ax, (0.7, .8, .5))


plt.show()