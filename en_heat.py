import numpy as np
import math
import sklearn
from sklearn.preprocessing import normalize
from genNormalDist import create_dataset

np.seterr(under='print')

n_samples = 500                         # número de samples
ep = 0.2                               # epsilon
t = 1                                   # parâmetro heat kernel
D = create_dataset(n_samples, [1, 1], [[0.1, 0], [0, 2]], [1, 1], [[0.9, 0.2], [0.2, 0.3]])
A = np.zeros((n_samples, n_samples))    # matriz de adjacência
G = np.zeros((n_samples, n_samples))    # grafo
W = np.zeros((n_samples, n_samples))    # weight de cada edge
G.flat[::n_samples + 1] = 1             # diagonal do grafo = 1

if(n_samples % 2 == 1):
    half_samples = int((n_samples / 2) + 1)
else:
    half_samples = int(n_samples / 2)

# normalizar matriz D
D = sklearn.preprocessing.normalize(D, axis=1, copy='false')

# (5409/2) + 1; a matriz é preenchida em ambos sentidos
# cria o grafo baseado em epsilon

for i in range(half_samples):
    for j in range((i + 1), n_samples):
        dist = np.sqrt(pow(D[i, 0] - D[j, 0], 2) + pow(D[i, 1] - D[j, 1], 2))
        A[i, j] = np.float64(dist)
        A[j, i] = A[i, j]
        
        if(A[i, j] < ep):
            G[i, j] = 1
            G[j, i] = 1

# calcular heat kernel
for i in range(half_samples):   
    for j in range((i + 1), n_samples):
        if(G[i, j] == 1):
            W[i, j] = np.float64(pow(math.e, -(A[i, j]) / t))
            W[j, i] = W[i, j]

# diagonal weight matrix e Laplacian matrix
dW = np.zeros((n_samples, n_samples))

for i in range(n_samples):
    for j in range(n_samples):
        dW[i, i] += W[j, i]
                
L = dW - W

# calcular eigenvectors e eigenvalues
vals, _vects = np.linalg.eig(L)
vects = _vects.transpose().copy()
cols = vals.argsort()
vals.sort()

for i in range(n_samples):
    vects[i] = _vects[:,cols[i]]

# vals = eigenvalues ordenados crescentemente
# vects2 = eigenvectors ordenados de acordo com seus respectivos eigenvalues
# Os eigenvectors e seus eigenvalues correspondentes se encontram nos mesmos
# indices em vals e vects2.

minA = A.min()
maxA = A.max()
avgA = np.average(A)
print("Min value A: ", minA)
print("Max value A: ", maxA)
print("Avg value A: ", avgA)
print("epsilon = ", ep)
# Soma dos termos da PA: (0+5408)*5409/2


