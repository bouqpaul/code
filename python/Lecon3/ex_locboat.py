from roblib import *

def f(x,u):
    x, u = x.flatten(), u.flatten()
    θ, v = x[2], x[3]
    xdot = array([[v * cos(θ)],
                  [v * sin(θ)],
                  [u[0]],
                  [u[1]]])
    return xdot

def g(x, u, m, dm):
    sinT = sin(x[2])
    cosT = cos(x[2])
    v = m - x[0:2]
    alpha = -x[2] + angle(v)
    dalpha = -u[0]+ (1 / norm(v)**2) * (v[0] * (dm[1] - x[3] * sinT) - v[1] * (dm[1] - x[3] * cosT))
    y = array([alpha, dalpha, x[2], x[3]])

    return y

def loc(u, y, m, dm):
    alpha = y[0][0]
    dalpha = y[1][0]
    theta = y[2][0]
    v = y[3][0]
    beta = theta + alpha
    dbeta = u[0][0] + dalpha
    tmp = array([[sin(beta), cos(beta)],
                  [-cos(beta), sin(beta)]])
    
    tmp2 = array([[-m[1][0], m[0][0]],
                  [m[0][0] - (dm[1][0] - v * sin(theta)) / dbeta, m[1][0] + (dm[0][0] - v * cos(theta)) / dbeta]])
    
    tmp3 = array([[cos(beta)],
                   [sin(beta)]])
    
    phat = tmp @ tmp2 @ tmp3
    return phat


x = array([[0],
           [0],
           [0],
           [1]])
    
u = array([[0.1],
           [0]])
dt = 0.1
fig 	= figure(0)
ax = fig.add_subplot(1, 1, 1, aspect='equal')

for t in np.arange(0, 20, dt):
    pause(0.01)  
    cla()
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    m = array([[6 + 2 * sin(t), 7 + 3 * cos(t)]]).T
    dm = array([[2 * cos(t), -3 * sin(t)]]).T
    draw_tank(x)
    y = g(x, u, m, dm)
    tmp = y.shape
    y = y + 0.001 * randn(tmp[0], tmp[1])
    
    phat = loc(u, y, m, dm)
    ax.plot(x[0], x[1], '+k')
    
    x = x + dt * f(x, u)
    ax.plot(m[0], m[1], '*r')
    
loc(u, y, m, dm)



