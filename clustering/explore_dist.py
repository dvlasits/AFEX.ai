import pandas as pd
from alignment import distance_matrix
from matplotlib import pyplot as plt
import datetime
from datetime import datetime
import numpy as np
import os

n = 10

data = pd.read_csv(os.path.join('data', 'dist_matrix_data.csv'))
dist = np.load('dist_matrix.npy')

dist *= 1-np.eye(len(dist))

print(dist.dtype)

dist = np.tanh(dist/100)
#dist = dist/np.max(dist)

#plt.hist(dist.flatten(), bins=50)
#plt.yscale('log')
#plt.show()


from sklearn.cluster import SpectralClustering

sc = SpectralClustering(n_clusters=10, affinity='precomputed')


clusters = sc.fit_predict(dist)
print(np.unique(clusters, return_counts=True))

data = pd.read_csv(os.path.join('data', 'dist_matrix_data.csv'))
clusters = pd.Series(clusters)


data = pd.concat([data, clusters.rename('cluster_id')], axis=1, join="inner")
print(data.head(5))

data.to_csv(os.path.join('data', 'clustered.csv'))