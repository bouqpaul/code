
from roblib import *
xhat = array([[0,1]]).T
Γx = array([[0.7,0.3],[0.3,0.2]])
fig = figure(0)
ax = fig.add_subplot(111)
ax.set_xlim(-1,12)
ax.set_ylim(-1,2)
draw_ellipse(xhat, Γx, 0.99,ax,'red')
pause(1)   