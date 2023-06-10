from sklearn.cluster import SpectralClustering
import numpy as np

sc = SpectralClustering(n_clusters=2, affinity='precomputed')

simil_mat = np.random.rand(5,5)
simil_mat = ((simil_mat-simil_mat.T)/2)**2
simil_mat += np.eye(5)
print(simil_mat)


clusters = sc.fit_predict(simil_mat)
print(clusters)

