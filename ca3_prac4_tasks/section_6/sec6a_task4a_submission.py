import pandas as pd
pd.set_option('display.width', None)

mydf = pd.read_excel("data/singstats_maritalstatus.xlsx")
mydf = mydf.set_index("Variables")

df_2010_and_after = mydf.filter(regex='^201')
print(df_2010_and_after)
