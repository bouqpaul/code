#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from roblib import *

NBR_TELEMETRES = 8

room = array([[3., 3., 1., 0., 0., 3., 3., 7., 8., 10., 10., 9., 9., 10., 10., 8., 7., 3.],
              [11., 8., 6., 6., 3., 3., 0., 0., 1.3, 1.3, 5.5, 5.5, 6.5, 6.5, 10., 10., 11., 11.]])  
                     
A = array([[0, 7, 7, 9, 9, 7, 7, 4, 2, 0 ,5, 6, 6, 5],
        [0, 0, 2, 2, 4, 4, 7, 7, 5, 5, 2, 2, 3, 3]
        ])
        
B = array([[7, 7, 9, 9, 7, 7, 4, 2, 0, 0, 6, 6, 5, 5],
            [0, 2, 2, 4, 4, 7, 7, 5, 5, 0, 2, 3, 3, 2]
            ])
            
y = array([6.4, 3.6, 2.3, 2.1, 1.7, 1.6, 3.0, 3.1])
y = y.reshape(len(y), 1)

def f(p, A, B):
    y = array([np.Infinity for i in range(NBR_TELEMETRES)])
    det = np.linalg.det
    for k in range(NBR_TELEMETRES):
        angleTemp = p[2] + k * (2 * np.pi / NBR_TELEMETRES)
        angleTemp = angleTemp[0]
        
        u = array([np.cos(angleTemp), np.sin(angleTemp)])
        u = u.reshape(len(u), 1)
        
        tempx = p[0][0]
        tempy = p[1][0]
        m = array([[tempx], [tempy]])
        
        for j in range(len(A[0])):
            a = A[:, j]
            b = B[:, j]
            
        a = a.reshape(len(a), 1)
        b = b.reshape(len(b), 1)
        
        AMU = np.concatenate((a - m, u), axis=1) #Cree la matrice à partir des colonnes a-m et u
        BMU = np.concatenate((b - m, u), axis=1)
        
        if det(AMU) * det(BMU) < 0:
            BAMA = np.concatenate((b - a, m - a), axis=1)
            BAU = np.concatenate((b - a, u), axis=1)
            
            alpha = -det(BAMA) / det(BAU)
            
            if alpha > 0:
                y[k] = min(alpha, y[k])
                
    y = y.reshape(len(y), 1)
    return y

def draw(p, y, A, B, fig, ax, line):
    temp = array([i for i in range(NBR_TELEMETRES)])
    temp = temp.reshape(len(temp), 1)
    
    theta = p[2] + temp * (2 * np.pi / NBR_TELEMETRES)
    
    shape = (2 * NBR_TELEMETRES, 1)
    X = np.zeros(shape)
    Y = np.zeros(shape)
    
    for i in range(0, (2 * NBR_TELEMETRES)):
        if i % 2 == 0:
            X[i] = p[0]
            Y[i] = p[1]
            
        else:
            tempIndice = (i) // 2
            X[i] = p[0] + y[tempIndice] * np.cos(theta[tempIndice])
            Y[i] = p[1] + y[tempIndice] * np.sin(theta[tempIndice])
    
    line.set_data(X, Y)
    fig.canvas.draw()
    pause(0.01)
    
    
plt.close("all")
fig = plt.figure()
plt.ion()
ax = fig.add_subplot(1, 1, 1)

for j in range(len(A[0])):
    Xtemp = [A[0, j], B[0, j]]
    Ytemp = [A[1, j], B[1, j]]
    lineRoom = ax.plot(Xtemp, Ytemp, 'k')
plt.show()
    
line = ax.plot([], [], color="r")[0]
plt.show()


p0 = array([6, 6, 0]).reshape(3, 1) #On commence au milieu de la piece
j0 = np.linalg.norm(y - f(p0, A, B))
T = 2
while(T > 0.01):
    p_essai = p0 + T * np.random.rand(3, 1)
    j_courant = np.linalg.norm(y - f(p_essai, A, B))
    
    draw(p_essai, y, A, B, fig, ax, line)
    
    if j_courant < j0:
        j0 = j_courant
        p0 = p_essai
        
    T *= 0.995
