# -*- coding: utf-8 -*-
from roblib import *

def init():
    plt.close("all")
    fig = plt.figure("Position")
    ax = fig.add_subplot(1, 1, 1)
    plt.xlim(-200, 900)
    plt.ylim(-400, 800)
    return (fig, ax)

def getData(path):
    data = []
    with open(path) as fichier:
        for line in fichier:
            line = line.split(" ")
            if line:
                tmp = [float(elt) for elt in line if elt != ""]
                data.append(tmp)
    data = array(data)
    return data

data = getData("./slam_data.txt")

def indiceTrouve(elt, lst):
    indice = 0
    while indice < len(lst):
        if lst[indice] == elt:
            return indice
        indice += 1
    return -1

T = array([[10540, 10920, 13740, 17480, 30380, 36880, 40240, 48170, 51720, 52320, 52790, 56880],
               [1, 2, 1, 0, 1, 5, 4, 3, 3, 4, 5, 1],
               [52.42, 12.47, 54.40, 52.68, 27.73, 26.98, 37.90, 36.71, 37.37, 31.03, 33.51, 15.05]
               ])  
    
def observ(k, nx, data, T):
    depth = data[:, 7]
    y = depth[k]
    phi = data[:, 1]
    theta = data[:, 2]
    psi = data[:, 3]
    vr = data[:, 4:7]
    alt = data[:, 8]
    
    C = zeros((1, nx))
    C[0, 2] = 1
    
    Gbeta = 0.01
    
    j = indiceTrouve(k, T[0, :])
    
    if j != -1:
        r = T[2, j]
        Rk = eulermat(phi[k], theta[k], psi[k])
        tmp = array([[0],
                     [-sqrt(abs(r**2 - (alt[k]**2)))],
                     [-alt[k]]
                     ])
        e = Rk @ tmp
        y = np.vstack((e[0:2], y))
        jm = 3 + 2 * T[1, j] + 1
        jm = int(jm)
        C = np.vstack((zeros((2, nx)), C))
        C[0, 0] = 1
        C[0, jm - 1] = -1
        C[1, 1] = 1
        C[1, jm] = -1
        Gbeta = diag([1, 1, 0.01])
        
    return (y, C, Gbeta)

def draw(k, xhat, Gx, ax, style):
    if(k % 300 == 0):
        draw_ellipse(xhat[0:2], Gx[0:2, 0:2], 0.9, ax, style)
        for i in arange(4, len(xhat), 2):
            draw_ellipse(xhat[i-1:i + 1], Gx[i-1:i + 1, i-1:i + 1], 0.9, ax, "red")
        plt.pause(0.01)

def smoother(data, ax, dt, nx, nm):
    kmax = len(data)

    u = [0 for elt in range(kmax)]
    
    x_forward = [0 for elt in range(kmax+1)]
    G_forward = [0 for elt in range(kmax+1)]
    
    xup = [0 for elt in range(kmax)]
    Gup = [0 for elt in range(kmax)]
    
    x_back = [0 for elt in range(kmax+1)]
    G_back = [0 for elt in range(kmax+1)]
    
    x_forward[0] = zeros((nx, 1))
    tmp = (10**5) * eye(2* nm)
    G_forward[0] = block_diag(0, 0, 0, tmp)
    Galpha = block_diag(0.01, 0.01, 0.01, eye(2 * nm))
    A = eye(nx)
    
    phi = data[:, 1]
    theta = data[:, 2]
    psi = data[:, 3]
    vr = data[:, 4:7]
    
    for k in range(kmax):
        tmp = eulermat(phi[k], theta[k], psi[k])
        tmp2 = vr[k, :].reshape(len(vr[k, :]), 1)
        tmp3 = dt * tmp @ tmp2
        
        u[k] = np.vstack((tmp3, zeros((2 * nm, 1))))
        
        y, C, Gbeta = observ(k, nx, data, T)
        
        x_forward[k+1], G_forward[k+1] = kalman(x_forward[k], G_forward[k], u[k], y, Galpha, Gbeta, A, C)
        
        xup[k], Gup[k] = kalman_correc(x_forward[k], G_forward[k], y, Gbeta, C)
        draw(k, x_forward[k], G_forward[k], ax, "b")
    
    x_back[kmax] = xup[-1]
    G_back[kmax] = Gup[-1]

    for k in arange(kmax - 1, -1, -1):
        J = Gup[k] @ (A.T) @ inv(G_forward[k+1])
        x_back[k] = xup[k] + J @ (x_back[k+1] - x_forward[k+1])
        G_back[k] = Gup[k] + J @ (G_back[k+1] - G_forward[k+1]) @ (J.T)
        draw(k, x_back[k], G_back[k], ax, 'k')
    
def Filter(data, ax, dt, nx, nm):
    xhat = zeros((nx, 1))
    tmp = (10**4) * eye(2* nm)
    Ghat = block_diag(0, 0, 0, tmp)
    Galpha = block_diag(0.01, 0.01, 0.01, eye(2 * nm))
    A = eye(nx)
    
    phi = data[:, 1]
    theta = data[:, 2]
    psi = data[:, 3]
    vr = data[:, 4:7]
#    
    kmax = len(data)
    
    for k in range(1, kmax):
        tmp = eulermat(phi[k], theta[k], psi[k])
        tmp2 = vr[k, :]
        tmp2 = tmp2.reshape(len(tmp2), 1)
        tmp3 = dt * tmp @ tmp2
        
        uk = np.vstack((tmp3, zeros((2 * nm, 1))))
        y, C, Gbeta = observ(k, nx, data, T)
        xhat, Ghat = kalman(xhat, Ghat, uk, y, Galpha, Gbeta, A, C)
        draw(k, xhat, Ghat, ax, "b")

def predict(data, ax, dt):
    phi = data[:, 1]
    theta = data[:, 2]
    psi = data[:, 3]
    vr = data[:, 4:7]
    
    xhat = array([[0],
                  [0],
                  [0]
                  ])
    Gx = diag([0, 0, 0])
    Galpha = 0.01 * eye(3)
    A = eye(3)
    kmax = len(data)
    
    y = eye(0, 1)
    Gbeta = eye(0, 0)
    C = eye(0, len(xhat))
    
    for k in range(1, kmax):
        tmp = eulermat(phi[k], theta[k], psi[k])
        tmp2 = vr[k, :]
        tmp2 = tmp2.reshape(len(tmp2), 1)
        uk = dt * tmp @ tmp2
    
        xhat, Gx = kalman(xhat, Gx, uk, y, Galpha, Gbeta, A, C)
        draw(k, xhat, Gx, ax, "b")

def slam(data):
    t = data[:, 0]
    
    depth = data[:, 7]
    alt = data[:, 8]
    
    dt = 0.1
    
    np = 3
    nm = 6
    nx = np + 2 * nm
    fig, ax = init()
#    predict(data, ax, dt)
#    Filter(data, ax, dt, nx, nm)
    smoother(data, ax, dt, nx, nm)
    
slam(data)
            