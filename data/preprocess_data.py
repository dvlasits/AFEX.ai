import pandas as pd

data = pd.read_csv('../download/pdb_data_no_dups.csv')
data = data[data['macromoleculeType'] == 'Protein']
data = data[['structureId', 'classification', 'residueCount']]

print(data.head(5))
print(data['classification'].value_counts().head(10))

# use top 8 classes
top = data['classification'].value_counts().head(8).index
print(top)

data = data[data['classification'].isin(top)]
print(data.head(10))

data.to_csv('labels.csv', index=False)