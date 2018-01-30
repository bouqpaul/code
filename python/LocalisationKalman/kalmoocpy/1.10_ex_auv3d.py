from roblib import *
fig = figure()
ax = Axes3D(fig)
             
def draw(x):
    x = x.flatten()    
    ax.clear()
    ax.set_xlim3d(-20,20)
    ax.set_ylim3d(-20,20)
    ax.set_zlim3d(0,40)
    M=array([ [0.0,0.0,10.0,0.0,0.0,10.0,0.0,0.0],
                   [-1.0,1.0,0.0,-1.0,-0.2,0.0,0.2,1.0],
                   [0.0,0.0,0.0,0.0,1.0,0.0,1.0,0.0]] )
    ax.plot(M[0],M[1],M[2],color='blue')        
    ax.scatter(0,0,0,color='magenta')
       
x = array([[0,0,10,15,0,1,0]]).T
u = array([[0,0,0.1]]).T
dt = 0.05
draw(x)
pause(1)
 
    