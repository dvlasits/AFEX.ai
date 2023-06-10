import pandas as pd
import numpy as np
from alignment import local_alignment_score, local_alignment_pair
data = pd.read_csv('../subsequences/with_representatives.csv')
from sklearn.linear_model import LogisticRegression
import pickle
def train(data):
    representatives = np.unique(data['representative'])
    scores = np.array([local_alignment_score(sequence,representative) for sequence in np.array(data['sequence']) for representative in representatives ]).reshape((len(data),len(representatives)))
    print(representatives)
    labels = data['classification']
    print(scores)
    clf = LogisticRegression(random_state=0, max_iter=10000).fit(scores, labels)
    filename = 'model.sav'
    pickle.dump(clf, open(filename, 'wb'))
    return clf

def predict(sequence, clf):
    representatives = np.unique(data['representative'])
    scores = np.array(
        [local_alignment_score(sequence, representative)  for representative
         in representatives]).reshape(1,len(representatives))

    reasons = [local_alignment_pair(sequence, representative)  for representative
         in representatives]
    return (clf.predict_proba(scores), reasons)

if __name__ == '__main__':
    clf = train(data)
    print(data.at[0, 'sequence'])
    print(predict(data.at[3, 'sequence'],clf))