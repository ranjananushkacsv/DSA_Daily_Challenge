'''
Build a function that computes pairwise cosine similarity between a query vector and a matrix of N document
vectors. Production retrieval systems call this millions of times, so loops are unacceptable.

Requirements:- 
Implement it fully vectorized with NumPy (no Python for-loops over rows).
Handle zero-vectors gracefully (return 0 similarity, no NaN/divide-by-zero).
Support both 1-D query vs 2-D matrix, and 2-D vs 2-D batched inputs

'''

import numpy as np

def cosine_similarity(querry,doc):
    querry = np.atleast_2d(querry)
    doc = np.atleast_2d(doc)

    dots = querry @ doc.T

    q_norm = np.linalg.norm(querry, axis = 1, keepdims = True)
    d_norm = np.linalg.norm(doc,axis = 1, keepdims = True)

    denom = q_norm @d_norm.T
    
    sims = np.divide(dots, denom, out=np.zeros_like(dots), where=denom != 0)

    return sims
