#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from roblib import *


n = 1000
Gx = array([[3, 1],[1, 3]])
xbar = array([[1], [2]])
b = np.random.randn(2, n)

#x = xbar @ ones((1, n)) + sqrtm(Gx) @ b
xbarLigne = xbar.reshape(1, len(xbar))[0]
x = np.random.multivariate_normal(xbarLigne, Gx, n).T

plt.close("all")
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(x[0, :], x[1, :], "r.")
draw_ellipse(xbar, Gx, 0.9, ax, (0, 0, 1))


x2 = arange(-10, 10, 0.1)
x1 = 1 + (x2 - 2) / 3
plt.plot(x1, x2, "g+")

x1 = arange(-10, 10, 0.1)
x2 = 2 + (x1 -1) / 3
plt.plot(x1, x2, "k+")

#plt.plot(b[0, :], b[1, :], "r.")
plt.show()