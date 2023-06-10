import numpy as np
import pandas as pd

aminoacids = np.array([c for c in "ACDEFGIKLMNPQRSTUVWY"])
assert(len(aminoacids) == 20)

def generate_random_sequence(n):
    indices = np.random.randint(0,20,n)
    return ''.join(aminoacids[indices])

# load cluster sequences
data = pd.read_csv('../data/clustering.csv')
data = data[data['0'] == 0]

N = 5

best = generate_random_sequence(N)
best_score = 999e99

for it in range(10000):
    if it % 1000 == 0:
        print(f"Iteration {it/1000}k, best score = {best_score}, best seq {best}")
    
    seq = generate_random_sequence(N)

    # get score

    if score < best_score:
        best_score = score
        best = seq

print(f"FINISHED! best score = {best_score}, best seq {best}")