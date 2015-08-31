import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize

def pca_plot(X, n_samples):
    groups = X[:, 2]
    X = np.delete(X, 2, 1)
    pca = PCA(n_components=1)
    pca.fit(X)
    X = pca.transform(X)
    x_values = (np.zeros((X.shape[0]))).transpose()
    for i in range(n_samples):
        if(groups[i] == 0):
            plt.plot(x_values[i], X[i,0], 'yo')
        else:
            plt.plot(x_values[i], X[i,0], 'go')
    plt.show()
#    return X
