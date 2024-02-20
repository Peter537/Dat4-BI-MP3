import numpy as np
import pandas as pd

# A custom library for calculating z-scores and identifying outlier
# calculate expects a panda dataframe

outliers = []

def calculate(data, threshold=3.0):
    
    # Start by clearing the outliers list
    outliers.clear()

    # Convert data to a pandas dataframe to use the mean and std functions
    data = pd.DataFrame(data)

    # Iterate through each column in the dataframe (from 2D to 1D)
    for column in data.columns:
        mean = data[column].mean()
        std = data[column].std()

        # Convert the column to a list to iterate through
        columnData = data[column].tolist()
        
        # Iterate through each point in the column
        for point in columnData:

            # Convert the point to a float if it is not already otherwise the z-score calculation will fail
            if not isinstance(point, float):
                point = float(point)
            z = (point - mean) / std

            # If the z-score is greater than the threshold, add the point to the outliers list
            if np.abs(z) > threshold:
                outliers.append(point)

def getOutliers(data, threshold=3.0):
    if len(outliers) == 0:
        calculate(data, threshold)
    return outliers