from genNormalDist import create_dataset
from en_heat import en_heat
from pca import pca_plot

# create_dataset(N, cov1, cov2, mean1=[1,1], mean2=[1,1])
# en_heat(n_samples, ep, t, D)

D = create_dataset(100, [[0.1, 0], [0, 2]], [[0.9, 0.2], [0.2, 0.3]])
en_heat(D.shape[0], 0.2, 1, D)
pca_plot(D, D.shape[0])

D1 = create_dataset(150, [[0.1, 1], [0, 2]], [[0.9, 0.2], [0.2, 0.3]], [5, 5]) # separados, alongado
en_heat(D1.shape[0], 0.2, 1, D1)
pca_plot(D1, D1.shape[0])

D2 = create_dataset(200, [[0.1, 0], [0, 8]], [[0.9, 0.2], [0.2, 0.3]]) # alongado sparse, escala aumenta para compensar
en_heat(D2.shape[0], 0.2, 1, D2)
pca_plot(D2, D2.shape[0])

D3 = create_dataset(300, [[3, 0], [0, 9]], [[1, 0.2], [0.2, 2.1]]) # circular non-sparse
en_heat(D3.shape[0], 0.2, 1, D3)
pca_plot(D3, D3.shape[0])

D4 = create_dataset(500, [[4, 0], [0, 2]], [[0.9, 0.2], [0.2, 0.3]]) # circular sparse
en_heat(D4.shape[0], 0.2, 1, D4)
pca_plot(D4, D4.shape[0])
