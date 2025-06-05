import pandas as pd

# USEFULL COMMANDS
# print(df.info())
# print(df.to_string())

# df = pd.read_csv("data.csv")
# print(df.head(5))

app_run = True

print("WELCOME\n")
add_file = input("File name: ")
analysis = pd.read_csv(add_file)
print(analysis.head(5))

while app_run:
    question = input("How do you want to deal with empty cells?\n"
                     "--> Press (1) to delete the rows containing empty cells\n"
                     "--> Press (2) to replace the values with the MEAN value of the column\n"
                     "--> Press (3) to replace the values with the MEDIAN value of the column\n"
                     "--> Press (4) to replace the values with the MODE value of the column\n"
                     "--> Press (q) to quit\n")

    if question == "1":
        print("TEST")

    elif question == "q":
        app_run = False
        print("GOODBYE")
