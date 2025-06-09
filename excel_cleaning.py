import pandas as pd
import numpy as np

print("\n### WELCOME ###\n")

while True:
    try:
        file_name = input("File name: ")
        df = pd.read_csv(file_name)
        break
    except FileNotFoundError:
        print("\nWrong file name, please try again.\n")

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
        app_run = False

    elif question == "2":
        df_numerical_col = (df.select_dtypes(include='number').columns.values.tolist())

        for col_name in df_numerical_col:
            df_mean = df[col_name].mean()
            df.fillna({col_name: df_mean}, inplace=True)

        print("\nSuccess! Missing values in the columns are now filled with the Mean value of each colum.")
        app_run = False

    elif question == "3":
        df_numerical_col = (df.select_dtypes(include='number').columns.values.tolist())

        for col_name in df_numerical_col:
            df_median = df[col_name].median()
            df.fillna({col_name: df_median}, inplace=True)

        print("\nSuccess! Missing values in the columns are now filled with the Median value of each colum.")
        app_run = False

    elif question == "4":
        df_numerical_col = (df.select_dtypes(include='number').columns.values.tolist())

        for col_name in df_numerical_col:
            df_mode = df[col_name].mode()[0]
            df.fillna({col_name: df_mode}, inplace=True)

        print("\nSuccess! Missing values in the columns are now filled with the Mode value of each colum.")
        app_run = False

    elif question == "q":
        app_run = False
        print("\n### GOODBYE ###")

    else:
        print("\nWrong input. Please try again.")

question2 = input("\n...")
