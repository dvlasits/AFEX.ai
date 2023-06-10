# AFEX.ai

<img width="525" alt="image" src="https://github.com/dvlasits/AFEX.ai/assets/11242884/0a9f6b39-3e22-4958-9b8f-9ad54fef6d75">

Amino Acid Functions Explained


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
