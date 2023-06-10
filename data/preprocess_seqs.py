import pandas as pd

# load sequences and labels
seqs = pd.read_csv('../download/pdb_data_seq.csv')
labels = pd.read_csv('labels_raw.csv')

# make sure sequence is available
seqs = seqs[seqs['sequence'].notnull()]

# use only labelled sequences
ids = labels['structureId']
seqs = seqs[seqs['structureId'].isin(ids)]

# drop duplicate sequences
seqs = seqs.drop_duplicates(subset='sequence', keep="first")

# use only proteins with single chain
counts = seqs['structureId'].value_counts()
counts = counts[counts == 1]
ids = counts.index

# use only ids in labels
ids = ids[ids.isin(labels['structureId'])]
ids = ids[ids.isin(seqs['structureId'])]

# drop duplicate labels
labels = labels.drop_duplicates(subset='structureId', keep="first")

# filter labels and seqs
labels = labels[labels['structureId'].isin(ids)]
seqs = seqs[seqs['structureId'].isin(ids)]

print(f"Seqs {len(seqs)}, labels {len(labels)}")

seqs = seqs[['structureId', 'sequence']]
seqs = seqs.set_index('structureId')
labels = labels.set_index('structureId')

#print(seqs.head(10))

data = pd.concat([seqs, labels], axis=1, join="inner")

print(data.head(10))

data.to_csv('all_data.csv')