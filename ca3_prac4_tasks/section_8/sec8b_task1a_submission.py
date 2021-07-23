import pandas as pd
pd.set_option('display.width', None)

mydf = pd.read_excel("data/singstats_maritalstatus.xlsx", na_values=['-'])
mydf = mydf.set_index("Variables")

print("**** First 10 rows of original dataset ****")
print(mydf.head(10))
print()
print("**** Remaining dataset after dropping columns with missing data ****")
print(mydf.dropna(axis='columns'))
