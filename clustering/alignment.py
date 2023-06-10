from Bio import Align
import pandas as pd
import numpy as np

def global_alignment_score(sequence1, sequence2):
    aligner = Align.PairwiseAligner(scoring='blastp')
    return aligner.align(sequence1,sequence2).score

def distance_between_two(df, id1, id2):
    row1 = df[id1]
    row2 = df[id2]
    sequence1 = row1.at[id1, 'sequence']
    sequence2 = row2.at[id2, 'sequence']
    return global_alignment_score(sequence1, sequence2)

def distance_matrix(df):
    n = len(df.index)
    matrix = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = distance_between_two(df,i,j)
    return matrix


if __name__ == '__main__':
    df = pd.read_csv('data/all_data.csv')
    df = df.head(10)
    print(distance_matrix(df))
