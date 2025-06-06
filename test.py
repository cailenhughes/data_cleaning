import pandas as pd

df = pd.read_csv("data.csv")
# df_columns = df.columns.values.tolist()
df_numerical_col = (df.select_dtypes(include='number').columns.values.tolist())

for col_name in df_numerical_col:
    # print(col_name)
    df_mean = df[col_name].mean()
    # print(df_mean)
    df.fillna({col_name: df_mean}, inplace=True)

print(df.to_string())
