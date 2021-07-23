import pandas as pd

mydf = pd.read_excel("data/singstats_maritalstatus.xlsx")
mydf = mydf.set_index("Variables")

print("*** Data in 1980 column ***")
print(mydf['1980'])
print()

rows_greater_500k = mydf['1980'] > 500000
total_rows_greater_500k = rows_greater_500k[rows_greater_500k == True].count()
total_rows_lesser_500k = rows_greater_500k[rows_greater_500k == False].count()

print("Number of rows more than 500k is {}".format(total_rows_greater_500k))
print("Number of rows less than 500k is {}".format(total_rows_lesser_500k))
