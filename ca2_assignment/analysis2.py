import sys
import numpy as np
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math


def calculate_histogram_range(min_value, max_value):
    hist_floor = int(math.floor(min_value / 100.0)) * 100
    hist_ceiling = int(math.ceil(max_value / 100.0)) * 100
    hist_range = np.arange(hist_floor, hist_ceiling+1, 100)
    return hist_range


def retrieve_data_from_mysql():
    user, pw, host, db = 'root', 'mysqladmin', 'localhost', 'ca2db'
    connection = mysql.connector.connect(user=user, password=pw, host=host, database=db, use_pure=True)
    cursor = connection.cursor()

    query_table = 'SELECT town, flat_type, price_per_sqft, price_per_month FROM resale_hdb WHERE purchase_year BETWEEN 2012 AND 2021'

    try:
        cursor.execute(query_table)
        data = pd.DataFrame(cursor.fetchall(),
                            columns=['town', 'flat_type', 'price_per_sqft', 'price_per_month'])
        connection.commit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        exit()
    finally:
        cursor.close()
        connection.close()

    print("Data Count (Saved Data): {}".format(data.shape[0]))
    return data


df = retrieve_data_from_mysql()
town_list = np.array(df.town.drop_duplicates())
town_count = 1
for town in town_list:
    print("{}. {}".format(str(town_count), town), end="\n")
    town_count += 1

town_choice = int(input("Please select your preferred town (key in numbering): "))
if town_choice > len(town_list) or town_choice < 1:
    print("Sorry, you have entered an invalid choice")
    print("Unable to continue. Exiting program....")
    exit()
town_index = town_choice - 1
town_selected = town_list[town_index]

# ======================
# GRAPH: 1 (BOXPLOT)
# ======================
df_selected = df[df.town.isin([town_selected]) &
                 df.flat_type.isin(['2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE'])]
df_selected = df_selected[['flat_type', 'price_per_sqft']]

boxplot_dict = sns.boxplot(data=df_selected, x='flat_type', y='price_per_sqft')

medians = df_selected.groupby(['flat_type'])['price_per_sqft'].median().astype(int)
vertical_offset = df_selected['price_per_sqft'].median() * 0.01
for xtick in boxplot_dict.get_xticks():
    boxplot_dict.text(xtick, medians[xtick] + vertical_offset, medians[xtick], horizontalalignment='center', color='w')

plt.suptitle("HDB RESALE PRICE in {} \n between Year 2012 to 2021".format(town_selected), fontsize=14, fontweight='bold')
plt.title("Median Price per Square Feet (sqft) by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Price per sqft (SGD)")

# ======================
# GRAPH: 2 (HISTOGRAM)
# ======================
df_graph2 = df[df.town.isin([town_selected])]
df_graph2 = df_graph2[['price_per_month']]
hist_range = calculate_histogram_range(df_graph2.min(), df_graph2.max())

df_graph2.hist(bins=hist_range, histtype='bar', ec='black')

axes = plt.gca()
axes.xaxis.grid()
plt.suptitle("HDB RESALE PRICE in {} \n between Year 2012 to 2021".format(town_selected), fontsize=14, fontweight='bold')
plt.title("Price per month from Purchase Date until End of Lease (usually 99 years)")
plt.xlabel("Price per month (SGD)")
plt.ylabel("Total Transaction")
plt.xticks(hist_range)
plt.show()
