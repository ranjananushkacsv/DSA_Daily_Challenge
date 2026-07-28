'''
You are handed a 5 GB CSV that does not fit in memory. Compute the per-column mean, variance, min, and
max in a single pass.

REQUIREMENTS
•Read the file in chunks (pandas chunksize or a manual reader).
•Use Welford's online algorithm for a numerically stable running mean/variance.
•Never load the full file into RAM.

'''
import pandas as pd
import numpy as np

import pandas as pd

def stream_stats(path, chunksize=100_000):
    stats = {}
    for chunk in pd.read_csv(path, chunksize=chunksize):
        for col in chunk.select_dtypes("number").columns:
            x = chunk[col].dropna().to_numpy()
            if x.size == 0:
                continue
            nB, meanB = x.size, x.mean()
            M2B = ((x - meanB) ** 2).sum()

            if col not in stats:
                stats[col] = {"n": nB, "mean": meanB, "M2": M2B,
                              "min": x.min(), "max": x.max()}
                continue

            a = stats[col]
            n = a["n"] + nB
            delta = meanB - a["mean"]
            a["mean"] += delta * nB / n
            a["M2"]   += M2B + delta**2 * a["n"] * nB / n
            a["n"]     = n
            a["min"]   = min(a["min"], x.min())
            a["max"]   = max(a["max"], x.max())

    return {c: {"mean": a["mean"], "var": a["M2"]/(a["n"]-1),
                "min": a["min"], "max": a["max"]}
            for c, a in stats.items()}

print(stream_stats("yourfile.csv"))