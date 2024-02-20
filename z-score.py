import numpy as np

outliers = []

def z_score(data, threshold=3.0):
    mean = np.mean(data)
    std = np.std(data)

    for d in data:
        z = (d - mean) / std
        if np.abs(z) > threshold:
            outliers.append(d)

def getOutliers(data, threshold=3.0):
    z_score(data, threshold)
    return outliers