#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#58:54

from roblib import *
from scipy.linalg import block_diag

landmarks = array([[0, 15, 30, 15],
                   [25, 30, 15, 20]
                   ])
dt = 0.1
      
def gonio(dt):
    plt.close("all")
    fig = plt.figure("Gonio")
    ax = fig.add_subplot(1,1,1)
    lim = 50
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])

    
    def f(x, u):
        xdot = array([x[3] * cos(x[4]) * cos([2]),
                      x[3] * cos(x[4]) * sin([2]),
                      x[3] * sin(x[4]) / 3,
                      u[0],
                      u[1]
                      ])
        return xdot
    
    def g(x):
        Ck = array([[0, 0, 1]])
        y = array([x[3]])
        Gbeta = eye(1)
#        logLst = []
        for i in range(len(landmarks[0])):
            a = landmarks[:, i]
            plt.plot(a[0], a[1], "+k")
            da = array([[a[0]],[a[1]]]) - x[0:2]
            dist = norm(da)
#            logLst.append("DIST n°{}: {:.2f}\n".format(i, dist))
            delta = np.arctan2(da[1], da[0]) - x[2]
            delta = delta[0]
            
            if dist < 25:
                yi = [[-a[0] * sin(x[2][0] + delta) + a[1] * cos(x[2][0] + delta)]]
                Cki = [[-sin(x[2][0] + delta), cos(x[2][0] + delta), 0]]
                plt.plot(a[0], a[1], "+r")
                
                y = np.append(y, yi, axis=0)
                
                Ck = np.append(Ck, Cki, axis=0)
                Gbeta = block_diag(Gbeta, 1.0)
                
        temp = mvnrnd2(zeros(y.shape), Gbeta)
        
        y = y + temp
        return (y, Gbeta, Ck)
    
    
    def gab(xa, xb):
        dab = xb[0:2] - xa[0:2]
        
        phi = (np.arctan2(dab[1], dab[0]) - xa[2])[0]
        yab = array([[0]])
        Gab = array([[1]])
        Cab = array([[0, 0, 0, 0, 0, 0]])
        dist = norm(dab)
#        print("DIST: ", dist)
        if dist < 35:
            plt.plot([xa[0], xb[0]],[xa[1], xb[1]], "xr")
            Cab = [[-sin(xa[2][0] + phi), cos(xa[2][0] + phi), 0,\
                    sin(xa[2][0] + phi), -cos(xa[2][0] + phi), 0]]
            
            Gab = array([[1]])
            yab = 0 + mvnrnd2([0], Gab)
        
        return (yab, Gab, Cab)
    
    def gall(xa, xb):
        ya, Ga, Cak = g(xa)
        yb, Gb, Cbk = g(xb)
        yab, Gab, Cab = gab(xa, xb)
        
        y = vstack((ya, yb, yab))
        Gbeta = block_diag(Ga, Gb, Gab)
        temp = block_diag(Cak, Cbk)
        Ck = vstack((temp, Cab))
        
        return (y, Gbeta, Ck)
    
    def onecar(dt):
        
        x = array([[0],
                   [-20],
                   [pi / 3],
                   [20],
                   [0.1]
                   ])
            
        u = array([[0],
                   [0],
                   [0]
                   ])
            
        zhat = array([[0],
                      [0],
                      [0]
                      ])
        
        Gz = 1000 * eye(3)
        Galpha = dt * 0.001 * eye(3)
        
        for t in arange(0, 5, dt):
            plt.cla()
            y, Gbeta, Ck = g(x)
            draw_car(x)
            
            delta = x[4]
            theta = x[2]
            
            Ak = eye(3) + dt * array([[0, 0, cos(delta) * cos(theta)],
                                 [0, 0, cos(delta) * sin(theta)],
                                 [0, 0, 0]
                                 ])
    
            uk = array([[0],
                        [0],
                        [dt * u[0]]
                        ])
            
            zhat, Gz = kalman(zhat, Gz, uk, y, Galpha, Gbeta, Ak, Ck)
            
            draw_ellipse(zhat[0:2], Gz[0:2:1, 0:2:1], 0.9, ax, "r")
            
            ax.set_xlim([-lim, lim])
            ax.set_ylim([-lim, lim])
            
            tmp = mvnrnd2(zeros((3, 1)), Galpha)
            
            alphax = 0 * x
            alphax[0], alphax[1], alphax[3] = tmp[0],tmp[1],tmp[2]
            x = x + dt * f(x, u) + alphax
            
            plt.pause(0.01)

    def twocars(dt):
        xa = array([[-13],
                   [-22],
                   [pi / 3],
                   [15],
                   [0.1]
                   ])
    
        xb = array([[20],
                   [-10],
                   [pi / 3],
                   [18],
                   [0.2]
                   ])
            
        ua = array([[0],
                   [0]
                   ])
        
        ub = array([[0],
                   [0]
                   ])
            
        zhat = array([[0],
                      [0],
                      [0],
                      [0],
                      [0],
                      [0]
                      ])
        
        Gz = 1000 * eye(6)
        GalphaA = dt * diag([0.1, 0.1, 0.5])
        GalphaB = dt * diag([0.1, 0.1, 0.5])
        Galpha = block_diag(GalphaA, GalphaB)
        for t in arange(0, 5, dt):
            plt.cla()
            y, Gbeta, Ck = gall(xa, xb)
            draw_car(xa)
            draw_car(xb)
            
            deltaA = xa[4]
            thetaA = xa[2]
            
            Aak = eye(3) + dt * array([[0, 0, cos(deltaA) * cos(thetaA)],
                                 [0, 0, cos(deltaA) * sin(thetaA)],
                                 [0, 0, 0]
                                 ])
            deltaB = xb[4]
            thetaB = xb[2]
            Abk = eye(3) + dt * array([[0, 0, cos(deltaB) * cos(thetaB)],
                                 [0, 0, cos(deltaB) * sin(thetaB)],
                                 [0, 0, 0]
                                 ])
            Ak = block_diag(Aak, Abk)
            uk = array([[0],
                        [0],
                        [dt * ua[0]],
                        [0],
                        [0],
                        [dt * ub[0]]
                        ])
            draw_ellipse(zhat[0:2], Gz[0:2:1, 0:2:1], 0.9, ax, "green")
            draw_ellipse(zhat[3:5], Gz[3:5:1, 3:5:1], 0.9, ax, "green")
            zhat, Gz = kalman(zhat, Gz, uk, y, Galpha, Gbeta, Ak, Ck)
            
            alphaA = 0 * xa
            tmp = mvnrnd2(zeros((3, 1)), GalphaA)
            alphaA[0], alphaA[1], alphaA[3] = tmp[0],tmp[1],tmp[2]
            
            alphaB = 0 * xb
            tmp = mvnrnd2(zeros((3, 1)), GalphaB)
            alphaB[0], alphaB[1], alphaB[3] = tmp[0],tmp[1],tmp[2]
            
            xa = xa + dt * f(xa, ua) + alphaA
            xb = xb + dt * f(xb, ub) + alphaB
            
            
            ax.set_xlim([-lim, lim])
            ax.set_ylim([-lim, lim])
            
            plt.pause(0.01)
            
    twocars(dt)    
        

gonio(dt)