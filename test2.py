import sys
import pandas as pd
import numpy as np

print("\n### WELCOME ###\n")

while True:
    try:
        file_name = input("File name: ")
        df = pd.read_csv(file_name)
        break
    except FileNotFoundError:
        print("\nWrong file name, please try again.\n"
              "Don't forget the extension (.csv or .xlsx) ;)\n")

print("\nFirst rows of your file:")
print(df.head(5))

print("\n### PART 1: CHECKING FOR ABNORMAL DATA ###")

app_run = True
df_num = df.select_dtypes(include='number')

outliers_dict = {}
mean_dict = {}

while app_run:
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

        outliers_dict[col_name] = outliers
        mean_dict[col_name] = mean

    question = input("\nHow do you want to deal with the abnormal values detected in column '" + col_name + "'?\n"
                     "--> Press (1) to keep them\n"
                     "--> Press (2) to delete them\n"
                     "--> Press (3) to replace them with the MEAN value of the column\n"
                     "--> Press (q) to quit\n"
                     "--> ")

    if question == "1":
        print("\nAbnormal values have not been modified.")
        app_run = False

    elif question == "2":
        deleted_rows = []

        for col_name, outliers in outliers_dict.items():
            for x in df.index:  # Delete rows containing outliers
                if df.loc[x, col_name] in outliers:
                    df.drop(x, inplace=True)
            deleted_rows.append(col_name)

        print("\nSuccess! Rows containing outliers have been deleted in column(s): '" + ", ".join(deleted_rows) + "'.")
        app_run = False

    elif question == "3":
        modified_rows = []

        for col_name, outliers in outliers_dict.items():
            mean = mean_dict[col_name]

            for x in df.index:  # Replace outliers with Mean value of the column
                if df.loc[x, col_name] in outliers:
                    df.loc[x, col_name] = mean
            modified_rows.append(col_name)

        print("\nSuccess! Rows containing outliers have been replaced by the mean value in columns: '"
              + ", ".join(modified_rows) + "'")
        app_run = False

    elif question == "q":
        print("\n### GOODBYE ###")
        app_run = False
        sys.exit(0)

print("\n### PART 2: DEALING WITH MISSING DATA ###")

app_run = True

while app_run:
    question2 = input("\nHow do you want to deal with empty cells?\n"
                      "--> Press (1) to delete the rows containing empty cells\n"
                      "--> Press (2) to replace the values with the MEAN value of the column\n"
                      "--> Press (3) to replace the values with the MEDIAN value of the column\n"
                      "--> Press (4) to replace the values with the MODE value of the column\n"
                      "--> Press (q) to quit\n"
                      "--> ")

    if question2 == "1":
        df = df.dropna()
        print("\nSuccess! Rows with missing values have been deleted.")
        app_run = False
        # TODO: find a way to count the deleted rows

    elif question2 == "2":
        df_numerical_col = (df.select_dtypes(include='number').columns.values.tolist())

        for col_name in df_numerical_col:
            df_mean = df[col_name].mean()
            df.fillna({col_name: df_mean}, inplace=True)

        print("\nSuccess! Missing values in the columns are now filled with the Mean value of each colum.")
        app_run = False

    elif question2 == "3":
        df_numerical_col = (df.select_dtypes(include='number').columns.values.tolist())

        for col_name in df_numerical_col:
            df_median = df[col_name].median()
            df.fillna({col_name: df_median}, inplace=True)

        print("\nSuccess! Missing values in the columns are now filled with the Median value of each colum.")
        app_run = False

    elif question2 == "4":
        df_numerical_col = (df.select_dtypes(include='number').columns.values.tolist())

        for col_name in df_numerical_col:
            df_mode = df[col_name].mode()[0]
            df.fillna({col_name: df_mode}, inplace=True)

        print("\nSuccess! Missing values in the columns are now filled with the Mode value of each colum.")
        app_run = False

    elif question2 == "q":
        app_run = False
        sys.exit(0)

print("\n### PART 3: SAVING CHANGES ###")

app_run = True

while app_run:
    question3 = input("\nDo you want to save your changes in a new file?"
                      "\n--> Press (1) to save your changes in a new .csv file."
                      "\n--> Press (2) to save your changes in a new .xlsx file."
                      "\n--> Press (q) to quit without saving your changes."
                      "\n--> ")

    if question3 == "1":
        df.to_csv('cleaned_data.csv', index=False)
        print("\nSuccess! Your changes have been saved in a new file called cleaned_data.csv.")
        app_run = False

    elif question3 == "2":
        df.to_excel('cleaned_data.xlsx', engine='xlsxwriter')
        print("\nSuccess! Your changes have been saved in a new file called cleaned_data.xlsx.")
        app_run = False

    elif question3 == "q":
        print("\n### GOODBYE ###")
        app_run = False
