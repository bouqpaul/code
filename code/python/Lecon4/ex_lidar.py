#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *
import csv
plt.close("all")
fig = plt.figure("Lidar")
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim([-.5, 3.5])
ax.set_ylim([-1.2, 2.8])

with open("lidar_data.csv", "r") as csvfile:
    tmp = csv.reader(csvfile, delimiter=";")
    A1 = []
    for row in tmp:
        A1.append(list(map(float, row)))

A1 = array(A1)
x1 = A1[:, 0]
y1 = A1[:, 1]
x1 = x1.reshape(len(x1), 1)
y1 = y1.reshape(len(y1), 1)
ax.plot(x1, y1, "+k")        
n = 10
d3 = []
alpha3 = []

for i in arange(1, len(A1) - n, n):
    x2 = x1[i-1:i+n-1]
    y2 = y1[i-1:i+n-1]

    A2 = np.hstack((x2, y2))
    b2 = ones((n, 1))
    p = (A2.T) @ A2
    p = inv(p)
    p = p @ A2.T
    p = p @ b2
    d2 = 1 / norm(p)
    alpha2 = np.arctan2(p[1], p[0])
    e = norm(A2 @ p - b2)

    if e < 0.05:
        ax.plot(x2, y2, "r*")
        d3.append(d2)
        alpha3.append(alpha2)
        
d3 = np.vstack(d3)
alpha3 = np.vstack(alpha3)

alpha3m = (1/4) * np.arctan2(median(sin(4 * alpha3)), median(cos(4 * alpha3)))

def indiceSup(vecteur, val):
    resultat = []
    for i in range(len(vecteur)):
        if vecteur[i] > val:
            resultat.append(i)

    resultat = np.vstack(resultat)
    return resultat

for k in range(3):
    alpha4 = (k * pi / 2) + alpha3m
    I = indiceSup(cos(alpha3 - alpha4), 0.9)
    tmpI = d3[I]
    d4 = np.median(tmpI)
    tmp1 = array([[1, 1]])
    tmp2 = array([[cos(alpha4)], [sin(alpha4)]])
    tmp3 = array([[-sin(alpha4)], [cos(alpha4)]])
    tmp4 = array([[-10, 10]])
    
    w = d4 * tmp2 @ tmp1 + tmp3 @ tmp4
    X = w[0, :]
    Y = w[1, :]
    ax.plot(X, Y, "b")



#n = 400
#alphav = pi / 3
#dv = 3
#xi = randn(n, 1)
#yi = ((dv - cos(alphav) * xi) / sin(alphav)) + 0.1 * randn(n, 1)
#plt.figure("Lidar")
#plt.plot(xi, yi, "+r")
#plt.show()

#print(alpha)
#print(d)

#n = 500
#alpha = (pi / 3) + 0.1 * randn(n, 1) + 2 * pi * np.floor(1.1 * rand(n, 1))
#alpha += np.floor(1.1 * rand(n, 1)) * 100 * randn(n, 1)
#plt.plot(cos(alpha), sin(alpha), "+k")
#plt.show()
#alpham = np.arctan2(np.median(sin(alpha)), np.median(cos(alpha)))
