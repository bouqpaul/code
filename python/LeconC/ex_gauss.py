# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#from roblib import *
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

plt.close('all')
Mx1 = np.arange(-5, 5, 0.01)
Mx2 = np.arange(-5, 5, 0.01)

X1, X2 = np.meshgrid(Mx1, Mx2)



xbar = np.array([[1],
              [2]])

mulA = np.array([[1, 0],
             [0, 2]])
A = np.array([[np.cos(pi/6), -np.sin(pi/6)],
            [np.sin(pi/6), np.cos(pi/6)]]) @ mulA


mulY = np.array([[2],
              [-5]])
ybar = A @ xbar + mulY



Gx = np.eye(2)
Gy = A * Gx * A
invGx = np.linalg.inv(Gx)
invGy = np.linalg.inv(Gy)

dX1 = X1 - xbar[0]
dX2 = X2 - xbar[1]

dY1 = X1 - ybar[0]
dY2 = X2 - ybar[1]

Qx = invGx[0, 0] * (dX1**2) + 2 * (invGx[0, 1] * dX1 * dX2) + invGx[1, 1] * (dX2**2)
Qy = invGy[0, 0] * (dY1**2) + 2 * (invGy[0, 1] * dY1 * dY2) + invGy[1, 1] * (dY2**2)

det = np.linalg.det
exp = np.exp

Zx = 1 / (2 * np.pi * np.sqrt(det(Gx))) * exp(-0.5 * Qx)
Zy = 1 / (2 * np.pi * np.sqrt(det(Gy))) * exp(-0.5 * Qy)

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection="3d")

ax.contour(X1, X2, Zx, 20)
ax.plot_surface(X1, X2, Zy, cmap=cm.coolwarm)