import numpy as np
import matplotlib.pyplot as plt

def create_dataset(N, mean1, cov1, mean2, cov2):

    if(N % 2 == 1):
        half_N = int((N / 2) + 1)
    else:
        half_N = int(N / 2)

    data = np.random.multivariate_normal(mean1, cov1, half_N)
    # print(L.shape)
    # (2, 2)
    half_N = N - half_N
    # print(data2.shape)
    # (2, 1000)
    data2 = np.random.multivariate_normal(mean2, cov2, half_N)
    plt.scatter(data2[:,0], data2[:,1], c='green')
    plt.scatter(data[:,0], data[:,1], c='yellow')

    maxScale = -1
    
    for i in range(2):
        if(cov1[i][i] > maxScale):
            maxScale = cov1[i][i]
        else:
            if(cov2[i][i] > maxScale):
                maxScale = cov2[i][i]

    maxScale = 3 * maxScale
    plt.xlim((-maxScale, maxScale))
    plt.ylim((-maxScale, maxScale))
    plt.show()
    return np.append(data, data2, axis=0)


#N = 250                         # número de samples
#mean = [1,1]                    # centro
#cov = [[0.3, 0.2],[0.2, 0.2]]   # matriz de covariância
#create_dataset(N, mean, cov)
