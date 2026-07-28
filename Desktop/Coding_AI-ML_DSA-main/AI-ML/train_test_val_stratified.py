''''
Implement a stratified splitter that preserves class proportions across train, validation, and test sets without
using sklearn's train_test_split.

REQUIREMENTS
Accept arbitrary split ratios (e.g., 70/15/15) that sum to 1.0.
Guarantee no sample appears in more than one split.
Make it deterministic via a random seed.
'''

import random

def stratified_split(X, y, ratios=(0.7, 0.15, 0.15), seed=42):
    random.seed(seed)                      # randomness fix

    
    classes = {}
    for i in range(len(y)):
        label = y[i]
        if label not in classes:
            classes[label] = []
        classes[label].append(i)

    train_idx, val_idx, test_idx = [], [], []

    for label in classes:
        idx = classes[label]
        random.shuffle(idx)

        n = len(idx)
        n_train = int(n * ratios[0])
        n_val = int(n * ratios[1])

        train_idx += idx[:n_train]
        val_idx += idx[n_train:n_train + n_val]
        test_idx += idx[n_train + n_val:]

    X_train = [X[i] for i in train_idx]
    y_train = [y[i] for i in train_idx]
    X_val = [X[i] for i in val_idx]
    y_val = [y[i] for i in val_idx]
    X_test = [X[i] for i in test_idx]
    y_test = [y[i] for i in test_idx]

    return X_train, y_train, X_val, y_val, X_test, y_test