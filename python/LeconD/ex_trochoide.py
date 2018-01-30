#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *

y = array([[0.38], [3.25], [4.97], [-0.26]])
t = array([[1], [2], [3], [7]])

pbar = array([[0], [0]])
Gp = 1000 * eye(2)

c1 = ones(len(t))
c2 = -cos(t)
C = np.column_stack((c1, c2))

Gbeta = 0.01 * eye(4)

ytilde = y - C @ pbar
Gy = C @ Gp @ (C.T) + Gbeta
K = Gp @ (C.T) @ np.linalg.inv(Gy)

phat = pbar + K @ ytilde
yhat = C @ phat
Geps = Gp - K @ C @ Gp


r = y - yhat
print(r)
t1 = arange(0, 10, 0.01)
x1 = phat[0] * t1 - phat[1] * sin(t1)
y1 = phat[0] - phat[1] * cos(t1)

plt.close("all")
plt.figure("Trochoïde")
plt.ion()
plt.plot(x1, y1, "r")

plt.figure("Altitude de la masse")
plt.plot(t1, y1, "r")
plt.plot(t, y, "k+")
plt.plot(t, yhat, "gx")
plt.show()