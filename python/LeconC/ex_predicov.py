#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from roblib import *

n = 5
b = np.random.rand(2, n)

Gx = array([[3, 1],
            [1, 3]])

xbar = array([[2],
              [3]])

#x = (xbar * ones((1, n))) + (sqrtm(Gx) @ b)
x = sqrtm(Gx) @ b




plt.close("all")
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.axis("square")
ax.set_xlim([-0.5, 2.5])
ax.set_ylim([-0.5, 2.5])

#line = ax.plot(x[0,:], x[1,:], 'r.')
print("X:\n", x)
print("b:\n", b)
#draw_ellipse(xbar, Gx, 0.9, ax, (0, 0, 1))
