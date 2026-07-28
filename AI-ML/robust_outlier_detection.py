'''
Build a configurable outlier handler that flags and optionally clips outliers using both the IQR method and
z-score, exposing it as a fit/transform component.

REQUIREMENTS
Support strategy='iqr' and strategy='zscore' with a configurable threshold.
Offer actions: 'flag' (return a boolean mask) or 'clip' (winsorize).
Fit on training data only; never leak test statistics.
'''

import numpy as np
import pandas as pd

def fir_outlier(x, strategy ='iqr', threshold= 1.5):
    x = np.asarray(x, dtype=float)
    lower, upper = [], []
    for col in range(x.shape[1]):
        values = x[:, col]
        if strategy == 'iqr':
            q1= np.percentile(values,25)
            q3= np.percentile(values,75)
            iqr = q3 - q1
            lo = q1 - threshold * iqr                 
            hi = q3 + threshold * iqr 
        elif strategy == 'zscore':                     
            mean = values.mean()                     
            std = values.std()                         
            lo = mean - threshold * std                
            hi = mean + threshold * std

        else:
            raise ValueError("only iqr or zscore")
        lower.append(lo)
        upper.append(hi)
    return {'lower': np.array(lower), 'upper': np.array(upper)}

def transform(x,params,action='flag'):
    x = np.asarray(x,dtype= float)
    lower, upper = params['lower'],params['upper']
    if action == 'flag':
        return(x<lower) | (x<upper)
    elif action == 'clip':
        return np.clip(x,lower, upper)
    else:
        raise ValueError("action can only be flag or clip")