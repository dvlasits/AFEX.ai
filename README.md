<img width="499" alt="Screenshot 2023-06-10 at 13 04 46" src="https://github.com/dvlasits/AFEX.ai/assets/11242884/23fa2fb9-9deb-4f51-b742-40fd5a4111b6">


Amino Acid Functions Explained

## The Problem


## The Process

<img width="975" alt="Screenshot 2023-06-10 at 15 06 51" src="https://github.com/dvlasits/AFEX.ai/assets/11242884/60748575-6289-439a-ae94-2a322f922ade">


## Clustering
https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html

## What is the problem
Understanding how cells work is hard and important for bio research and medicine. Lots of high quality data can be obtained from RNAseq or proteomics, but interpretation is hard.

RNAseq and proteomics provide only protein sequence, at least in the first step.

Understanding the protein interactions and their roles is important so we undestand how cell works and how we can treat diseases.

We're building explainable ML model to tell us what the individual proteins do and how we know.

### How are we different
People are already trying to use large models to predict protein function - but this is unexplainable blackbox.

Our model could be improved by using 3D structural data from AlphaFold, to understand spatial interactions - this would be the next iteration of our model.

Identifying important sequences could also give us insight on how proteins work and how can we engineer them

## Example application
Treating cancer.

Take RNAseq data from cells from tumour and from healthy patient. We want to use the data to rationalize what caused the cancer and what targets (proteins) can we use to treat it.

The data obviously contains lots of noise (proteins very much depend on sex, age, diet, tissue type), so it's hard to find what bits of data are relevant to cancer.

By understanding the protein functions we can rationalize the differences in RNAseq and how they relate to cancer.

Understanding how the specific proteins contribute to cancer helps us decide which proteins are good targets.

## Daniels pitch

2 Main ones as far as I can tell:

- Someone is sick, we want to know which proteins are the causing the issue, 
- If we know what parts of protiens create different functions, we can engineer new proteins
- This requires being able to clearly justify and explain the functions of proteins due to sequences of amino acids

How, good old fashioned computer science and bioinformatics:

Bioinformatics cocktail.

What is the Problem:

Answers the question "What is life?" lol

Want to explain the data - not just stick an LLM at it and call it deep.

How do we solve it?


Are you sure?


Can you do it?



The Process:

Large dataset of labelled proteins.

Pairwise alignment - gives distance matrix

Get similarity matrix somehow

Then perform Markov Clustering

For every cluster we find a sequence that represents that cluster

Local-Alignment
