#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *
import numpy as np

plt.close("all")
fig = plt.figure("Distwall")
ax = fig.add_subplot(1,1,1)

ax.set_xlim([-20, 40])
ax.set_ylim([-20, 40])

A = array([[2, 15, 3], [1, 5, 12]])
B = array([[15, 3, 2], [5, 12, 1]])
C = array([])
dbar = array([])

for i in range(len(A[0])):
    temp = B[:, i] - A[:, i]
    u = (temp) / norm(temp)
    C = np.append(C, [[-u[1], u[0]]])
    dbar = np.append(dbar, [det((u, -A[:, i]))])

C = C.reshape(3, 2)
d = array([[2], [5], [4]])
dbar = array([dbar])
dbar = dbar.reshape(len(dbar[0]), 1)
y = d - dbar
x0 = array([[1], [2]])
G0 = 100 * eye(2)
u = 0
Galpha = 0 * G0
Gbeta = eye(3)
tmp = eye(2)


#C = array([C])

x1, G1 = kalman(x0, G0, u, y, Galpha, Gbeta, tmp, C)

for i in range(len(A[0])):
    plt.plot([A[0, i], B[0, i]],[A[1, i], B[1, i]], 'k')
    draw_disk(x1, d[i], ax, "blue")
    draw_ellipse(x0, G0, 0.9, ax, "k")
    draw_ellipse(x1, G1, 0.9, ax, "red")

plt.show()