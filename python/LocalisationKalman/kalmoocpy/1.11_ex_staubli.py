from roblib import * 
fig = figure()
ax = Axes3D(fig)  
 
def draw():
    ax.clear()
    ax.set_xlim3d(-2,2)
    ax.set_ylim3d(-2,2)
    ax.set_zlim3d(0,2)
    J = array([[0, 1, 0, 0, 0] , [0, 0, 1, 0,0] , [0, 0, 0, 1,0] , [1, 1, 1, 1,1]])
    plot3D(ax,J,"black",2)
    pause(0.01)
        
        
draw()    
pause(1)
        
