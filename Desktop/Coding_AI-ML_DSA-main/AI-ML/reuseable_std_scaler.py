'''
Create a reuseable standard scaler class for scaling transforms
scaler is basically something that puts your data into normal scale
Most common of them being standard scaler. Z = (x-mean)/S.D

Write a Scaler class with the sklearn fit / transform / inverse_transform API. This is the contract every
preprocessing step in a pipeline must honor.
REQUIREMENTS

fit() stores mean and std; transform() standardizes; inverse_transform() recovers the original.
Raise a clear error if transform is called before fit.
Handle constant columns (std == 0) without producing NaNs.

'''

import numpy as np

class Scaler:
    def __init__(self):
        self.mean_ = None   # will store column means after fit
        self.std_ = None    # will store column stds after fit

    def fit(self, X):
        X = np.asarray(X, dtype=float)
        self.mean_ = X.mean(axis=0)     # mean of each column
        self.std_ = X.std(axis=0)       # std of each column
        # constant column fix: if std is 0, set it to 1 so we don't divide by zero
        self.std_[self.std_ == 0] = 1.0
        return self                     # return self so you can chain: Scaler().fit(X)

    def transform(self, X):
        if self.mean_ is None:          # was fit ever called?
            raise RuntimeError("Scaler not fitted yet. Call fit() first.")
        X = np.asarray(X, dtype=float)
        return (X - self.mean_) / self.std_

    def inverse_transform(self, X):
        if self.mean_ is None:
            raise RuntimeError("Scaler not fitted yet. Call fit() first.")
        X = np.asarray(X, dtype=float)
        return X * self.std_ + self.mean_   # reverse of transform