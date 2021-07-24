import pandas as pd
import matplotlib.pyplot as plt

df_rainfall = pd.read_csv("data/rainfall-monthly-total.csv")
df_rainfall = df_rainfall.set_index('month')

rain_greater_300mm = df_rainfall[df_rainfall.total_rainfall > 300]
rain_greater_300mm = rain_greater_300mm.sort_values(by='total_rainfall')
rain_greater_300mm = rain_greater_300mm.tail(12)

rain_greater_300mm.plot(kind='bar')
plt.legend(loc='upper left')
plt.show()
