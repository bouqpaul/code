# -*- coding: utf-8 -*-
"""
@author: Jordan NININ
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# attention au sens des variables suivant l'utilisation de ode ou de odeint
def f(y,t):
    d1 = 10*(y[1]-y[0])
    d2 = 28*y[0]-y[1]-y[0]*y[2]
    d3 = y[0]*y[1]-8/3 * y[2]
    return np.array([d1,d2,d3])
    
    
def jacobian_y(y,t):
    l1 = [-10, 10, 0]
    l2 = [28-y[2], -1, -y[0]]
    l3 = [y[1], y[0], -8/3]
    return np.array([l1,l2,l3])
    
def schema_taylor2(t,y,h):
    ynew= y +h*(f(y,t) ) +((h**2)/2)*(jacobian_y(y,t)@f(y,t))
    return ynew
    
    
def Taylor(t0,tmax,h,y0):
    T= np.arange(t0,tmax+h,h)
    Y=[]
    y = y0
    for t in T:
        Y.append(y)
        y = schema_taylor2(t,y,h)
    return T,Y

    
def euler(t0,tmax,h,y0,f):
    T= np.arange(t0,tmax+h,h)
    Y=[]
    y = y0
    for t in T:
        Y.append(y)
        y= y+h*f(y,t)
    return T,Y

    
if __name__=="__main__":
    y0 = np.array([1,2,3])
    T1, Y1 = Taylor(0,10,0.01,y0)
    T2 = T1 
    Y2 = odeint(f,y0,T2)
    T3, Y3 = euler(0,10,0.0001,y0,f)
    
    
    Y1 = np.array(Y1).T
    Y2 = np.array(Y2).T
    Y3 = np.array(Y3).T
    
    
    plt.figure()
    plt.plot(T1,Y1[0,:],'r')
    plt.plot(T2,Y2[0,:],'b')
    plt.plot(T3,Y3[0,:],'g')
    plt.show()
    
    plt.figure()
    
    plt.plot(Y1[0,:],Y1[1,:],'r')
    plt.plot(Y2[0,:],Y2[1,:],'b')
    plt.plot(Y3[0,:],Y3[1,:],'g')
    plt.show()