#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
import roblib as rl
importlib.reload(rl)

# plt.close("all")
# plt.ion()
# 
# NBR = 5000
# x = array([i for i in range(NBR)]).reshape(1, NBR)
# y = np.random.randn(1, NBR)
# 
# for i in range(10):
#     y = array([y[0][:-1] + y[0][1:]])
# plt.figure()
# plt.plot(x, y, "r+")
# 
# indice0 = [i for i in range(NBR - 100)]
# indice1 = [i for i in range(1, NBR - 99)]
# 
# a = y[0][indice0]
# b = y[0][indice1]
# plt.figure()
# plt.plot(a, b, "r+")
# plt.show()

A0 = rl.array([[.5, 0], [0, 1]])
A1 = rl.array([[1, -1], [1, 1]])
A2 = A1

u0 = rl.array([[8], [16]])
u1 = rl.array([[-6], [-18]])
u2 = rl.array([[32], [-8]])

C0 = rl.array([[1, 1]])
C2 = C1 = C0

y0 = 7
y1 = 30
y2 = -6

Galpha = rl.eye(2)
Gbeta = 1

xhat0 = rl.array([[0], [0]])
Gx0 = 100 * eye(2)

rl.close("all")
rl.ion()
fig = rl.figure("Kalman 3 steps")
ax = fig.add_subplot(1, 1, 1)

rl.draw_ellipse(xhat0, Gx0, 0.9, ax, "black")
# --------------------------------
xhat1, Gx1 = rl.kalman(xhat0, Gx0, u0, y0, Galpha, Gbeta, A0, C0)
rl.draw_ellipse(xhat1, Gx1, 0.9, ax, "red")

xup0, Gup0 = rl.kalman_correc(xhat0, Gx0, y0, Gbeta, C0)
rl.draw_ellipse(xup0, Gup0, 0.9, ax, "black", style="--")
# --------------------------------
xhat2, Gx2 = rl.kalman(xhat1, Gx1, u1, y1, Galpha, Gbeta, A1, C1)
rl.draw_ellipse(xhat2, Gx2, 0.9, ax, "green")

xup1, Gup1 = rl.kalman_correc(xhat1, Gx1, y1, Gbeta, C1)
rl.draw_ellipse(xup1, Gup1, 0.9, ax, "red", style="--")
# --------------------------------
xhat3, Gx3 = rl.kalman(xhat2, Gx2, u2, y2, Galpha, Gbeta, A2, C2)
rl.draw_ellipse(xhat3, Gx3, 0.9, ax, "magenta")

xup2, Gup2 = rl.kalman_correc(xhat2, Gx2, y2, Gbeta, C2)
rl.draw_ellipse(xup2, Gup2, 0.9, ax, "green", style="--")

# --------------------------------

ax.set_xlim([-25, 25])
ax.set_ylim([-40, 40])

rl.show()