from roblib import *

fichier = open("slam_data.txt",'r')
D = fichier.read()
fichier.close()
D = D.split("\n")
for i in range(len(D)):
    D[i] = D[i].split(" ")
    while True:
        try :
            D[i].remove('')
        except:
            break

D = [ [float(elt) for elt in Ligne] for Ligne in D]
D = array ( D[0:len(D)-1] ) #suppression de la dernière ligne car elle est vide

t = D[:,0]
phi = D[:,1]
theta = D[:,2]
psi = D[:,3]
vr = D[:, 4:7].T
pz = D[:,7]
a = D[:,8]

xhat = zeros((5,1))

xhat[-2] = 602
xhat[-1] = 475

dt = t[1] - t[0]
#Gx = diag([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1])*10**6
#Galpha = diag([0.01,0.01,0.01,0,0,0,0,0,0,0,0,0,0,0,0])

#Gx = diag([0, 0, 0, 1, 1])*10**6
Gx = diag([0, 0, 0, 1, 1])
Galpha = diag([0.01, 0.01, 0.01, 0, 0])

A = eye(5)

def g(i):
#    T = array([[10540,10920,13740,17480,30380,36880,40240,48170,51720,52320,52790,56880],
#               [1,2,1,0,1,5,4,3,3,4,5,1],
#               [52.42,12.47,54.40,52.68,27.73,26.98,37.90,36.71,37.37,31.03,33.51,15.05]])

    T = array([[10540, 13740, 30380, 56880],
               [1, 1, 1, 1],
               [52.42, 54.40, 26.98, 15.05]])
    y = array([[pz[i]]])
#    C = array([[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]])
    C = array([[0, 0, 1, 0, 0]])
    Gbeta = 0.1*eye(1)
    if i in T[0]:
        j = list(T[0]).index(i)
        k = int(T[1,j])
        rk = T[2,j]
        yi = R @ array([[0, -sqrt(rk**2 - a[i]**2), -a[i]]]).T
        y = vstack((yi[0:2,:], y))
#        Ci = hstack((eye(2,3), zeros((2,2*k)), -eye(2), zeros((2, 12 - 2 * (k + 1)))))
        Ci = hstack((eye(2,3), -eye(2)))
        C = vstack((Ci, C))
        Gbeta = 0.1 * eye(3)
    return y, C, Gbeta


ax = init_figure(-200, 900, -300, 800)
N = len(t)

#x = array([[602],
#           [475]])
#    
#G = eye(2)
#draw_ellipse(x, G, 0.99, ax, "green")

for i in range(N):
    R = eulermat(phi[i],theta[i],psi[i])
    v = vr[:, i].reshape(3,1)
#    u = vstack((dt * R @ v, zeros((12, 1))))
    u = vstack((dt * R @ v, zeros((2, 1))))
    y, C, Gbeta = g(i)
    
    xup, Gup = kalman_correc(xhat, Gx, y, Gbeta, C)
    xhat,Gx = kalman_predict(xup, Gup, u, Galpha, A)
    
    if i % 300 == 0:
        draw_ellipse(xhat[0:2], Gx[0:2, 0:2], 0.99, ax, [0.4, 0.4, 1])
        draw_ellipse(xhat[-2:], Gx[-2:, -2:], 0.9, ax, "red")
#        for i in arange(4, len(xhat), 2):
#            draw_ellipse(xhat[i-1:i + 1], Gx[i-1:i + 1, i-1:i + 1], 0.9, ax, "red")
        
        pause(0.01)