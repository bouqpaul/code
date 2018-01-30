from roblib import *
import numpy as np

u= array([2, -1, 1, -1, 1, -1, 1, -1])
k= array([0,1,2,3,4,5,6,7])
#Y= array([[0],[-1],[-2],[3],[7],[11],[16],[36]])
Y= array([0,-1,-2,3,7,11,16,36])

y=Y[2:8]


M= array([-Y[1:7].reshape(6), -Y[0:6].reshape(6), u[1:7].reshape(6), -u[0:6].reshape(6)])
M=M.T

phat= ((np.linalg.inv((M.T) @ M)) @ (M.T)) @ y

yhat= M @ phat
print("P chapeau:\n", phat)
print("Y chapeau:\n", yhat)

#print(phat)