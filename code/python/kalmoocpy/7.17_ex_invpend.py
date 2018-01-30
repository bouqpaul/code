from roblib import *
M,l,g,m = 5,1,9.81,1
dt = 0.05

x = array([[0,2.5,0,0]]).T
Γα = 0.00001*eye(4)

def draw_invpend(a,θ,ax): #inverted pendulum
    draw_box(a-0.7,a+0.7,-0.25,0,ax,'blue')
    plot( [a,a-sin(θ)],[0,cos(θ)],'magenta', linewidth = 2)  

def f(x,u):
    a,θ,da,dθ=x[0,0],x[1,0],x[2,0],x[3,0]
    dda=(m*sin(θ)*(g*cos(θ)- l*dθ**2) + u)/(M+m*sin(θ)**2)
    ddθ= (sin(θ)*((m+M)*g - m*l*dθ**2*cos(θ)) + cos(θ)*u)/ (l*(M+m*sin(θ)**2))
    return(array([[da],[dθ],[dda],[ddθ]]))
    
fig = figure(0)    
ax = fig.add_subplot(111, aspect='equal')

for t in arange(0,5,dt) :
    pause(0.01) 
    cla()       
    ax.set_xlim(-3,3)
    ax.set_ylim(-3,3)         
    draw_invpend(x[0,0],x[1,0],ax)
    u = 0
    α=mvnrnd1(Γα)
    x = x + dt*f(x,u)+α  
pause(1)    
    