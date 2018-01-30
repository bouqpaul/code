# -*- coding: utf-8 -*-
from roblib import *
from scipy import signal

def f(x, u, l=1, M=1, m=1, g=9.81):
    x1 = x[1]
    x3 = x[3]
    v = array([x[2],
               x3,
               [(m * sin(x1) * (g * cos(x1) - l * x3**2) + u) / (M + m * sin(x1)**2)],
               [(sin(x1) * ((M + m) * g - m * l * (x3**2) * cos(x1)) + u * cos(x1)) / (l * (M + m * sin(x1)**2))]
               ])
    return v

def draw(x, w, l=1):
    plt.cla()
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.plot([x[0], x[0] - l * sin(x[1])], [0, l * cos(x[1])], "blue")
    plt.plot(x[0] + [-0.5, 0.5, 0.5, -0.5, -0.5], [0, 0, -0.25, -0.25, 0], "red")
    plt.plot(w, 0, "+r")
    plt.pause(0.01)


def invpend():
    plt.close("all")
    fig = plt.figure("Pendule Inverse")
    ax = fig.add_subplot(1, 1, 1)
    l = 1
    M = 5
    g = 9.81
    m = 1
    dt = 0.1
    A = array([[0, 0, 1, 0],
               [0, 0, 0, 1],
               [0, m * g / M, 0, 0],
               [0, (M + m) * g / (l * M), 0, 0]
               ])
    
    B = array([[0],
               [0],
               [1 / M],
               [1 / (l * M) ]
               ])
    
    poles = [-2, -2.1, -2.2, -2.3]
    K = (signal.place_poles(A, B, poles)).gain_matrix
    E =  array([[1, 0, 0, 0]])
    C = array([[1, 0, 0, 0],
               [0, 1, 0, 0]
               ])
    At = A.T
    Ct = C.T
#    L = ((signal.place_poles(At, Ct, poles)).gain_matrix).T
    h = -inv(E @ inv(A - B @ K) @ B)
    
    x = array([[0],
               [0.1],
               [0],
               [0]
               ])
    
    xhat = array([[0],
                  [0],
                  [0],
                  [0]
                  ])
    Gx = eye(4)
    Galpha = dt * 0.001 *  eye(4)
    Gbeta = (0.01**2) * eye(2)
    for i in arange(0, 10, dt):
        w = 2
        u = -K @ xhat + h * w
        y = C @ x + 0.01 * np.random.randn(2, 1)
#        xhat = xhat + dt * (A @ xhat + B @ u - L @ (C @ xhat - y))
        xhat, Gx = kalman(xhat, Gx, dt * B @ u, y, Galpha, Gbeta, eye(4) + dt * A, C)
        x = x + dt * f(x, u, l=l, M=M, m=m)
        draw(x, w, l=l)

invpend()