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
    outliers = col_values[np.abs(z_scores) > 3.5]

    if outliers.size != 0:
        print("Some abnormal values have been detected in column '" + col_name + "':", outliers)

    for x in df_num.index:
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
        break

    elif question == "2":
        for x in df.index:
            if df.loc[x, col_name] in outliers:
                df.drop(x, inplace=True)
                print(df.to_string())

    elif question == "3":
        for x in df.index:
            if df.loc[x, col_name] in outliers:
                df.loc[x, col_name] = mean
                print(df.to_string())

'''
col_values = df_num["maxpulse"].dropna().values
median = np.median(col_values)
deviations = np.abs(col_values - median)
mad = np.median(deviations)
z_scores = (0.6745 * (col_values - median)) / mad
outliers = col_values[np.abs(z_scores) > 3.5]
print("Some abnormal values have been detected in column '" + "duration" + "':", outliers)

for x in df.index:
    if df.loc[x, "duration"] in outliers:
        df.drop(x, inplace=True)
        print(df.to_string())

    mean = df["duration"].mean()
    df.fillna({"duration": mean}, inplace=True)
    print(mean)
'''