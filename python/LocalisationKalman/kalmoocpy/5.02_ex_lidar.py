from roblib import *

def parse(path):
	fichier = open(path, 'r')
	D 		= fichier.read()
	fichier.close()
	D 		= D.split("\n")

	for i in range(len(D)):
		D[i] = D[i].split(";")
		while True:
			try :
				D[i].remove('')
			except:
				break

	D 		= [ [float(elt) for elt in Ligne] for Ligne in D]
	data 	= array ( D[0:len(D)-1] ) #☺suppression de la dernière ligne car elle est vide
	return data
 

data = array(parse("lidar_data.csv"))

n = 10

Y = data[:, 1]
Y = Y.reshape((len(Y),1))
X = data[:, 0].reshape((len(Y),1))

d = []
alpha = []

for i in range(X.shape[0]//n):
    Xi = X[i*n:(i+1)*n,:]
    Yi = Y[i*n:(i+1)*n,:]
    plot(Xi,Yi,color='black')
