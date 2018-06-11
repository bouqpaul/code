# -*- coding: utf-8 -*-
"""
@author: Jordan NININ
"""


import numpy as np
import matplotlib.pyplot as plt


def f1(t,y):
    d0 = y[1]
    d1 = (1/y[2])*(-9.81*np.sin(y[0]) -2*y[1]*y[3])
    d2 = y[3]
    d3 = y[2]*y[1]**2+9.81*np.cos(y[0])-10*(y[2]-1)
    return np.array([d0,d1,d2,d3])
    
    
    
def euler(t0,tmax,h,y0,f):
    T= np.arange(t0,tmax+h,h)
    Y=[]
    y = y0
    for t in T:
        Y.append(y)
        y= y+h*f(t,y)
    return T,Y
    

    
def RK2(t0,tmax,h,y0,f):
    
    T= np.arange(t0,tmax+h,h)
    Y=[]
    y = y0
    for t in T:
        Y.append(y)
        k1 = h*f(t  ,y )
        k2 = h*f(t+h,y + k1)
        y= y+ 1/2*k1 + 1/2*k2
    return T,Y
        

if __name__=="__main__":
    y0 = np.array([-np.pi/4,0,1,0])
    T1, Y1 = euler(0,10,0.00001,y0,f1)
    T2, Y2 = RK2(0,10,0.001,y0,f1)
    
    Y1 = np.array(Y1).T
    Y2 = np.array(Y2).T
    
    
    plt.figure()
    plt.plot(Y1[2,:]*np.sin(Y1[0,:]),-Y1[2,:]*np.cos(Y1[0,:]),'r')
    plt.plot(Y2[2,:]*np.sin(Y2[0,:]),-Y2[2,:]*np.cos(Y2[0,:]),'b')
    plt.show()
    
    