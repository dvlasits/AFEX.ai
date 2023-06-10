# CALCULATES DISTANCE MATRIX FOR SUBSET OF DATA AND SAVES THE DISTANCE MATRIX

import pandas as pd
from alignment import distance_matrix
from matplotlib import pyplot as plt
import datetime
from datetime import datetime
import numpy as np

n = 300

data = pd.read_csv('../data/all_data.csv')
data = data.sample(frac=n/len(data)).reset_index(drop=True)

data.to_csv('dist_matrix_data.csv', index=False)

start = datetime.now()

dist = distance_matrix(data, is_global=False)

print(f"Elapsed {datetime.now() - start}, {n} sequences")

np.save('dist_matrix.npy', dist)
print("Distance matrix saved!")

