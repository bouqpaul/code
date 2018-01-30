from roblib import *
import matplotlib.pyplot as plt

NBR_POINTS = 100

P = 2 * np.random.rand(NBR_POINTS, 2)
y = array([[0], [1], [2.65] , [4.885], [7.646], [10.882]] )

ym = array([0,0,0,0,0,0])
ym= ym.reshape(len(ym), 1)

epsilon = 1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)


for p in P: 
    a, b = p[0], p[1]
    
    A = array([[1,     0],
             [a,    0.9]
             ])
    
    B = array([[b],
              [1-b]
              ])
    
    C = array([1,1])
    x = ([[0],[0]])
    
    
    for k in np.arange(len(ym)):
        x1 = A @ x + B
        ym[k] = C @ x
        x = x1
    
    if np.linalg.norm(ym - y, ord=np.inf) < epsilon:
        plot(a, b, 'rs')
        
    else:
        plot(a, b, 'b.')
        
plt.show()           

        
