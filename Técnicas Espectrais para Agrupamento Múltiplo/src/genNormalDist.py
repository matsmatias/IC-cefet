import numpy as np
import matplotlib.pyplot as plt

def create_dataset(N, cov1, cov2, mean1=[1,1], mean2=[1,1]):

    group = np.zeros((N, 1))
    
    if(N % 2 == 1):
        half_N = int((N / 2) + 1)
    else:
        half_N = int(N / 2)

    for i in range(half_N, N):
        group[i] = 1
    
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
    R = np.append(data, data2, axis=0)
    return np.append(R, group, axis=1)


#N = 501                         # número de samples
#cov1 = [[0.3, 0.2],[0.2, 0.2]]   # matriz de covariância
#cov2 = [[0.3, 0.2],[0.2, 0.9]]   # matriz de covariância
#D = create_dataset(N, cov1, cov2)
