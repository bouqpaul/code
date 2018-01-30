# -*- coding: utf-8 -*-

from roblib import *

plt.close("all")
plt.figure("Pendule")
plt.show()

def f(x, u):
    xdot = array([x[1],
                  [-sin(x[0]) + u]
                  ])
    return xdot
    
    
def draw(a, col):
    plot(sin(a), -cos(a), col)
    plot([0, sin(a)], [0, -cos(a)], col)

dt = 0.1
sigmX = 0.05
x = array([[0],
           [0]
           ])
    
xr = array([[0],
            [0]
            ])
    
P = eye(2)
Galpha = dt * (sigmX**2)
sigmY = 0.1
Gbeta = sigmY**2
C = array([[0, 1]])

for t in arange(0, 10, dt):
    cla()
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    
    y = C @ x + sigmY * randn()
    w, dw, ddw = sin(t), cos(t), -sin(t)
    draw(w, "red")
    draw(xr[0], "green")
    draw(x[0], "k")
    covXR = (5**2) * P[0, 0]
    
    centre = array([[0],
                    [0]])
    
    a = array([[sin(xr[0] - covXR)],
                [-cos(xr[0] - covXR)]
                ])
    
    draw_arc(centre, a, 2 * covXR, "blue")
    
    u = sin(xr[0]) + (w - xr[0]) + 2 * (dw - xr[1]) + ddw
    
    A = array([[1, dt],
               [-dt * cos(xr[0]), 1]])
    
    V = dt * array([[0],
                    [-sin(xr[0])+xr[0] * cos(xr[0]) + u],
                    ])
    
    xr, P = kalman(xr, P, V, y, Galpha, Gbeta, A, C)
    
    x = x + dt * f(x, u) + sigmX * sqrt(dt) * randn(2, 1)
    pause(0.01)