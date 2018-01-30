from roblib import *

def f(x):
    x=x.flatten()
    return (array([[1],[2],[1],[2]]))

def draw(x): 
    draw_disk(array([[0],[0]]),r,ax,"grey")
    θ=x[0,0]
    α=x[1,0]
    p=array([r*cos(θ),r*sin(θ)])
    β=α+θ
    plot( array( [p[0], p[0]-l1*cos(β)]), array([p[1], p[1]-l1*sin(β)]),'blue')  # pendulum down
    plot( array( [p[0], p[0]+l2*cos(β)]), array([p[1], p[1]+l2*sin(β)]),'red')   # pendulum high
        
r=10
l1=1
l2=(-r+sqrt(r**2+4*(l1*r-l1**2)))/2;
g = 9.81
dt=0.05;
x=array([[1],[0.2],[0],[0]])

fig = figure(0)    
ax = fig.add_subplot(111, aspect='equal')

for t in arange(0,5,dt) :
    pause(0.01) 
    cla()       
    ax.set_xlim(-12,12)
    ax.set_ylim(-12,12)         
    draw(x)  
    a=randn()
    x=x+dt*f(x); 
    


 