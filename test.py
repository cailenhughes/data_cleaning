import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

col_values = df["duration"].dropna().values
median = np.median(col_values)
deviations = np.abs(col_values - median)
mad = np.median(deviations)
z_scores = (0.6745 * (col_values - median)) / mad
outliers = col_values[np.abs(z_scores) > 3.5]

print("Some abnormal values have been detected in your file:", outliers)

