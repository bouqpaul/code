#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *

U = [4, 10, 10, 13, 15]
Tr = [0, 1, 5, 5, 3]

C = np.column_stack((U, Tr))

y = array([[5, 10, 8, 14, 17]])
y = y.reshape(len(y[0]), 1)

Gx = array([[4, 0], [0, 4]])

xbar = array([[1], [-1]])

Gbeta = 9 * eye(5)


ytilde = y - C @ xbar
Gy = C @ Gx @ C.T + Gbeta
K = Gx @ (C.T) @ np.linalg.inv(Gy)

xhat = xbar + K @ ytilde
Geps = Gx - K @ C @ Gx
yhat = C @ xhat
r = y - yhat
print(r)