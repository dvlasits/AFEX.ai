import numpy as np
import pandas as pd
from alignment import average_alignment_score
import os
aminoacids = np.array([c for c in "ACDEFGIKLMNPQRSTUVWY"])
assert(len(aminoacids) == 20)

def generate_random_sequence(n):
    indices = np.random.randint(0,20,n)
    return ''.join(aminoacids[indices])

def get_score(candidate, df, cluster_id):
    # print(df.loc[df['cluster_id'] == cluster_id].head(10))
    # clusters = df.cluster_id.unique()
    return average_alignment_score(candidate, df.loc[df['cluster_id'] == cluster_id])

if __name__ == '__main__':
    # load cluster sequences
    data = pd.read_csv(os.path.join('data', 'clustered.csv'))

    N = 8

    best = generate_random_sequence(N)
    best_score = 0
    clusters = sorted(data.cluster_id.unique())
    best_scores = np.zeros_like(clusters)
    best_sequences = np.array([best for _ in clusters])


    for it in range(100):
        if it % 100 == 0:
            print(f"Iteration {it/1000}k, best scores = {best_scores}, best seqs {best_sequences}")

        seq = generate_random_sequence(N)
        cluster_scores = np.array([get_score(seq,data,cluster) for cluster in clusters])
        cluster_scores = cluster_scores * (1+1./len(cluster_scores)) - np.average(cluster_scores)
        for i in range(len(cluster_scores)):
            if cluster_scores[i] > best_scores[i]:
                best_scores[i] = cluster_scores[i]
                best_sequences[i] = seq
    # print((np.rint(np.array(data['cluster_id'])).astype(int)))
    print(type(best_sequences))

    data.loc[:,'representative'] = best_sequences[(np.rint(np.array(data['cluster_id'])).astype(int))]

    print(data.head(10))


    print(f"FINISHED! best scores = {best_scores}, best seqs {best_sequences}")
    data.to_csv(os.path.join('data', 'with_representatives.csv'))