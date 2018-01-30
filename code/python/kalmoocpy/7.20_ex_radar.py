from roblib import *
                  
def g(x):
    g1 = norm(x[::2,:]-a)**2
    g2 = norm(x[::2,:]-b)**2
    return(array([[g1],[g2]]))
    
dt = 0.02
Γα = diag([0,dt,0,dt])
Γβ = eye(2)
x  = array([[0],[0],[2],[0]])
a = array([[0,0]]).T
b = array([[1,0]]).T
Ak=array([[1,dt,0,0],[0,1-dt,0,0],[0,0,1,dt],[0,0,0,1-dt]])

fig = figure(0)
ax = fig.add_subplot(111, aspect='equal')

for t in arange(0,1,dt) :
    pause(0.01)  
    cla()
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    y = g(x) +  mvnrnd1(Γβ)
    uk=array([[0]]*4)
    plot(a[0],a[1],'o')
    plot(b[0],b[1],'o')
    plot(x[0,0],x[2,0],'o')    
    draw_disk(a,sqrt(y[0,0]),ax,[0.8,0.8,0.8])
    draw_disk(b,sqrt(y[1,0]),ax,[0.8,0.8,0.8])   
    x = Ak @ x + mvnrnd1(Γα)
pause(1)