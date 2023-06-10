from Bio import Align
import pandas as pd
import numpy as np

def global_alignment_score(sequence1, sequence2):
    aligner = Align.PairwiseAligner(scoring='blastp')
    return aligner.align(sequence1,sequence2).score

def local_alignment_score(sequence1, sequence2):
    aligner = Align.PairwiseAligner(scoring='blastp')
    aligner.mode = 'local'
    return aligner.align(sequence1,sequence2).score

def distance_between_two(df, id1, id2, distance_function):
    sequence1 = df.at[id1, 'sequence']
    sequence2 = df.at[id2, 'sequence']
    return distance_function(sequence1, sequence2)

def distance_matrix(df, is_global = True):
    df = df.reset_index()
    n = len(df.index)
    matrix = np.zeros((n,n))
    distance_function = global_alignment_score
    if not is_global:
        distance_function = local_alignment_score
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j] = distance_between_two(df,i,j, distance_function)
    
    matrix += matrix.T
    return matrix

def average_alignment_score(sequence1, df, is_global = False):
    df = df.reset_index()
    n = len(df.index)
    scores = np.zeros(n)
    distance_function = global_alignment_score
    if not is_global:
        distance_function = local_alignment_score
    for i in range(n):
        sequence2 = df.at[i, 'sequence']
        scores[i]= distance_function(sequence1, sequence2)

    return np.average(scores)

if __name__ == '__main__':
    df = pd.read_csv('data/all_data.csv')
    df = df.head(10)
    print(distance_matrix(df, is_global=False))
