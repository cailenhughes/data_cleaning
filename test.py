import pandas as pd

while True:
    try:
        file_name = input("File name: ")
        df = pd.read_csv(file_name)
        break
    except FileNotFoundError:
        print("Wrong file name, please try again.")
