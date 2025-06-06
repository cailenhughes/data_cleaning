import pandas as pd

# USEFULL COMMANDS
# df = pd.read_csv("data.csv")
# print(df.info())
# print(df.to_string())
# print(df.head(5))

print("\n### WELCOME ###\n")

file_name = input("File name: ")
df = pd.read_csv(file_name)
print("\nFirst rows of your file:")
print(df.head(5))

app_run = True

while app_run:
    question = input("\nHow do you want to deal with empty cells?\n"
                     "--> Press (1) to delete the rows containing empty cells\n"
                     "--> Press (2) to replace the values with the MEAN value of the column\n"
                     "--> Press (3) to replace the values with the MEDIAN value of the column\n"
                     "--> Press (4) to replace the values with the MODE value of the column\n"
                     "--> Press (q) to quit\n"
                     "--> ")

    if question == "1":
        df_delete = df.dropna()
        rows_deleted = len(df.index.values.tolist()) - len(df_delete.index.values.tolist())
        print("\nSuccess! Number of rows deleted:", rows_deleted)
        break

    elif question == "2":
        df_numerical_col = (df.select_dtypes(include='number').columns.values.tolist())

        for col_name in df_numerical_col:
            # print(col_name)
            df_mean = df[col_name].mean()
            # print(df_mean)
            df.fillna({col_name: df_mean}, inplace=True)

        print("\nSuccess! Missing values in the columns are now filled with the mean value of each colum.")
        break

    elif question == "q":
        app_run = False
        print("\n### GOODBYE ###")
