import pandas as pd
from alignment import distance_matrix

data = pd.read_csv('../data/all_data.csv')
data = data.sample(frac=100/len(data)).reset_index(drop=True)

print(data.head(10))

print(data['classification'].value_counts())

dist = distance_matrix(data)