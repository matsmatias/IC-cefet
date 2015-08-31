import numpy as np
import math
import sklearn
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from genNormalDist import create_dataset

def en_heat(n_samples, ep, t, D):
        
        A = np.zeros((n_samples, n_samples))    # matriz de adjacência
        G = np.zeros((n_samples, n_samples))    # grafo
        W = np.zeros((n_samples, n_samples))    # weight de cada edge
        G.flat[::n_samples + 1] = 1             # diagonal do grafo = 1

        if(n_samples % 2 == 1):
                half_samples = int((n_samples / 2) + 1)
        else:
                half_samples = int(n_samples / 2)

        # remover última coluna de D
        groups = D[:, 2]
        D = np.delete(D, 2, 1)

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

        for i in range(n_samples):
                if(groups[i] == 0):
                        plt.plot([vects[i, 1]], 'yo')
                else:
                        plt.plot([vects[i, 1]], 'go')
                        
        plt.show()

        # vals = eigenvalues ordenados crescentemente
        # vects = eigenvectors ordenados de acordo com seus respectivos eigenvalues
        # Os eigenvectors e seus eigenvalues correspondentes se encontram nos mesmos
        # indices em vals e vects2.

        #minA = A.min()
        #maxA = A.max()
        #avgA = np.average(A)

