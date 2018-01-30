# -*- coding: utf-8 -*-

from roblib import *
import numpy as np

pi = np.pi

A1 = np.array([[1, 0],
               [0, 3]])

angle = pi/4
A2 = np.array([[np.cos(angle), -np.sin(angle)],
                [np.sin(angle), np.cos(angle)]])

G1 = np.eye(2)
G2 =  3 * np.eye(2)

G3 = A1 @ G2 @ (A1.T) + G1
G4 = A2 @ G3 @ (A2.T)

G5 = G4 + G3
G6 = A2 @ G5 @ (A2.T)

plt.close("all")
plt.ion()
fig = plt.figure("Ellipses de confiance")
ax = fig.add_subplot(1,1,1)

plt.axis("square")
ax.set_xlim([-15, 15])
ax.set_ylim([-15, 15])

draw_ellipse(array([[0],[0]]), G1, 0.9, ax, (1, 0, 0))
draw_ellipse(array([[0],[0]]), G2, 0.9, ax, (0, 1, 0))
draw_ellipse(array([[0],[0]]), G3, 0.9, ax, (0.5, 0, 1))
draw_ellipse(array([[0],[0]]), G4, 0.9, ax, (0, 0.5, 1))
draw_ellipse(array([[0],[0]]), G5, 0.9, ax, (0.5, 1, 0))
draw_ellipse(array([[0],[0]]), G6, 0.9, ax, (0, 1, 1))

