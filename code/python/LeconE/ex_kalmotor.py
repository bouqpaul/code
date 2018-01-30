#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
import roblib as rl
importlib.reload(rl)

y = rl.array([[5], [10], [11], [14], [17]])
C = rl.array([[4, 0], [10, 1], [10, 5], [13, 5], [15, 3]])
A = rl.eye(2)
xhat = rl.array([[1], [-1]])
Gx = 4 * rl.eye(2)
Galpha = rl.zeros((2, 2))
u = rl.zeros((2, 1))
Gbeta = 9


rl.close("all")
rl.ion()
fig = rl.figure("Kalman Motor CC")
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(-4, 6)
ax.set_ylim(-6, 4)

rl.draw_ellipse(xhat, Gx, 0.9, ax, "red")

for i in range(len(y)):
    Ctemp = array([C[i, :]])
    xhat, Gx = rl.kalman(xhat, Gx, u, y[i], Galpha, Gbeta, A, Ctemp)
    rl.draw_ellipse(xhat, Gx, 0.9, ax, "blue")

plt.show()