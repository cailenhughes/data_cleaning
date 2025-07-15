import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
df_num = df.select_dtypes(include='number')
outliers_dict = {}
mean_dict = {}

print(df.info())

for col_name in df_num:
    col_values = df_num[col_name].dropna().values
    median = np.median(col_values)
    deviations = np.abs(col_values - median)
    mad = np.median(deviations)
    z_scores = (0.6745 * (col_values - median)) / mad
    outliers = col_values[np.abs(z_scores) > 3.5]  # Checking for potential outliers in each column

    if outliers.size == 0:  # Size of the array containing outliers = 0, so no outlier for the column
        continue

    print("Some abnormal values have been detected in column '" + col_name + "':", outliers)

    for x in df_num.index:  # Calculate the Mean value of the column (without considering the potential outliers)
        if df_num.loc[x, col_name] in outliers:
            df_num.drop(x, inplace=True)

        mean = df_num[col_name].mean()
        df_num.fillna({col_name: mean}, inplace=True)

    outliers_dict[col_name] = outliers
    mean_dict[col_name] = mean
    
question = input("\nHow do you want to deal with these values?\n"
                 "--> Press (1) to keep them\n"
                 "--> Press (2) to delete them\n"
                 "--> Press (3) to replace them with the MEAN value of the column\n"
                 "--> Press (q) to quit\n"
                 "--> ")

if question == "1":
    print("\nAbnormal values have not been modified.")

elif question == "2":
    deleted_rows = []

    for col_name, outliers in outliers_dict.items():
        for x in df.index:  # Delete rows containing outliers
            if df.loc[x, col_name] in outliers:
                df.drop(x, inplace=True)
        deleted_rows.append(col_name)

    print("\nSuccess! Rows containing outliers have been deleted in column(s): '" + ", ".join(deleted_rows) + "'.")

elif question == "3":
    modified_rows = []

    for col_name, outliers in outliers_dict.items():
        mean = mean_dict[col_name]

        for x in df.index:  # Replace outliers with Mean value of the column
            if df.loc[x, col_name] in outliers:
                df.loc[x, col_name] = mean
        modified_rows.append(col_name)

    print("\nSuccess! Rows containing outliers have been replaced by the mean value in columns: '" + ", ".join(modified_rows) + "'")
