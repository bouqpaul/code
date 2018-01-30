#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *

y = array([[8], 
            [7],
            [0]])

C = array([[2, 3], [3, 2], [1, -1]])
            
xbar = array([[0],
                [0]])

Gx = 10000 * eye(2)
ybar = C @ xbar
ytilde = y - C @ xbar
Gbeta = array([[1, 0, 0],[0, 4, 0],[0, 0, 4]])
Gy = C @ Gx @ (C.T) + Gbeta
K = Gx @ (C.T) @ np.linalg.inv(Gy)

xhat = xbar + K @ ytilde

Geps = Gx - K @ C @ Gx
yhat = C @ xhat

err = y - yhat
print("Xhat:\n", xhat)
print("Yhat:\n", yhat)
print("Ecart:\n", err)