import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
df_num = df.select_dtypes(include='number')

for col_name in df_num:
    col_values = df_num[col_name].dropna().values
    median = np.median(col_values)
    deviations = np.abs(col_values - median)
    mad = np.median(deviations)
    z_scores = (0.6745 * (col_values - median)) / mad
    outliers = col_values[np.abs(z_scores) > 3.5]  # Checking for potential outliers in each column

    if outliers.size == 0:  # Size of the array containing outliers = 0, so no outlier for the column
        continue

    print("\nSome abnormal values have been detected in column '" + col_name + "':", outliers)

    for x in df_num.index:  # Calculate the Mean value of the column (without considering the potential outliers)
        if df_num.loc[x, col_name] in outliers:
            df_num.drop(x, inplace=True)

        mean = df_num[col_name].mean()
        df_num.fillna({col_name: mean}, inplace=True)

    question = input("\nHow do you want to deal with these values?\n"
                     "--> Press (1) to keep them\n"
                     "--> Press (2) to delete them\n"
                     "--> Press (3) to replace them with the MEAN value of the column\n"
                     "--> Press (q) to quit\n"
                     "--> ")

    if question == "1":
        continue

    elif question == "2":
        for x in df.index:  # Delete rows containing outliers
            if df.loc[x, col_name] in outliers:
                df.drop(x, inplace=True)
                print(df.to_string())

    elif question == "3":
        for x in df.index:  # Replace outliers with Mean value of the column
            if df.loc[x, col_name] in outliers:
                df.loc[x, col_name] = mean
                print(df.to_string())

df.to_excel('out2.xlsx', engine='xlsxwriter')
