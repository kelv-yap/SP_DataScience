from pylab import text
from datetime import datetime
import os
import numpy as np
import matplotlib.pyplot as plt
import math


def calculate_price_per_square_feet(resale_price, square_meter_area):
    convert_sm_to_sqft = 10.7639
    square_feet_area = np.round(square_meter_area * convert_sm_to_sqft)
    per_sqft = np.round(resale_price / square_feet_area, 2)
    return per_sqft


def calculate_price_per_month(purchase_year, lease_year, resale_price):
    lease = 99
    lease_remaining_year = np.array(lease_year) + np.array(lease) - np.array(purchase_year)
    lease_remaining_month = lease_remaining_year * 12
    price_per_month = np.round(resale_price / lease_remaining_month, 2)
    return price_per_month


def calculate_histogram_range(min_value, max_value):
    hist_floor = int(math.floor(min_value / 100.0)) * 100
    hist_ceiling = int(math.ceil(max_value / 100.0)) * 100
    hist_range = np.arange(hist_floor, hist_ceiling+1, 100)
    return hist_range


if os.path.exists('data/clean_data.csv'):
    os.remove("data/clean_data.csv")
csv_data1 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv", skiprows=1, delimiter=",", dtype=str)
csv_data2 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv", skiprows=1, delimiter=",", dtype=str)
csv_data3 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv", skiprows=1, delimiter=",", dtype=str)

combined_data_count = len(csv_data1) + len(csv_data2) + len(csv_data3)
print("Data Count (Before Concatenate): " + str(combined_data_count))

combined_data = np.concatenate((csv_data1, csv_data2, csv_data3), axis=0)
del csv_data1, csv_data2, csv_data3
print("Data Count (After Concatenate): {}".format(len(combined_data)))

np.savetxt("data/clean_data.csv",
           combined_data,
           delimiter=",",
           fmt=['%s', '%s', '%s', '%s', '%s', '%s'],
           header='purchase_date, town, flat_type, floor_area_sqm, lease_commence_year, resale_price')
del combined_data

saved_data = np.genfromtxt("data/clean_data.csv",
                           delimiter=",",
                           dtype=[('purchase_date', 'U10'),
                                  ('town', 'U30'),
                                  ('flat_type', 'U30'),
                                  ('floor_area_sqm', 'i4'),
                                  ('lease_commence_year', 'U10'),
                                  ('resale_price', 'i4')]
                           )
print("Saved Data counts: {}".format(len(saved_data)))

town_list = np.unique(saved_data['town'])
town_count = 1
for town in town_list:
    print("{}. {}".format(str(town_count), town), end="\n")
    town_count += 1

town_choice = int(input("Please select your preferred town (key in numbering): "))
town_index = town_choice - 1
town_selected = town_list[town_index]
if town_choice > len(town_list) or town_choice < 1:
    print("Sorry, you have entered an invalid choice")
    print("Unable to continue. Exiting program....")

# ======================
# GRAPH: 1 (BOXPLOT)
# ======================
filtered_data_by_flat_type = saved_data[np.isin(saved_data['flat_type'], ['2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE'])]
hdb_type = np.unique(filtered_data_by_flat_type['flat_type'])

filtered_data_by_flat_type['purchase_date'] = [datetime.strptime(date, '%Y-%m').year for date in filtered_data_by_flat_type['purchase_date']]
years = np.array([int(i) for i in (np.unique(filtered_data_by_flat_type['purchase_date']))])

x_label = []
data_by_room_type = []

for type in hdb_type:
    filtered_data = filtered_data_by_flat_type[np.isin(filtered_data_by_flat_type['flat_type'], [type]) &
                                               np.isin(filtered_data_by_flat_type['town'], [town_selected])]

    has_elements = filtered_data.size > 0
    if has_elements:
        x_label.append("{} \n Total: {}".format(type, len(filtered_data)))
        resale_price = filtered_data['resale_price']
        square_meter_area = filtered_data['floor_area_sqm']
        per_sqft = calculate_price_per_square_feet(resale_price, square_meter_area)
        data_by_room_type.append(per_sqft)

plt.figure(1)
plt.subplot(111)
plt.suptitle("HDB RESALE PRICE in {} \n between Year {} to {}".format(town_selected, years.min(), years.max()), fontsize=14, fontweight='bold')
plt.title("Price per Square Feet (sqft) by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Price per sqft (SGD)")
# plt.boxplot(np.array(data_by_room_type), labels=x_label)
boxplot_dictionary = plt.boxplot(np.array(data_by_room_type), labels=x_label)
for line in boxplot_dictionary['medians']:
    x, y = line.get_xydata()[1] # top of median line
    text(x, y, int(y), horizontalalignment='right') # draw above, centered

# ======================
# GRAPH: 2 (HISTOGRAM)
# ======================
filtered_data_by_town = saved_data[np.isin(saved_data['town'], [town_selected])]
filtered_data_by_town['purchase_date'] = [datetime.strptime(date, '%Y-%m').year for date in filtered_data_by_town['purchase_date']]

data_by_price_per_month = calculate_price_per_month([int(i) for i in filtered_data_by_town['purchase_date']],
                                                    [int(i) for i in filtered_data_by_town['lease_commence_year']],
                                                    filtered_data_by_town['resale_price'])

hist_range = calculate_histogram_range(data_by_price_per_month.min(), data_by_price_per_month.max())

plt.figure(2)
plt.subplot(111)
# plt.hist(plot_data, range=(x_min, x_max), bins=x_bin)
plt.hist(data_by_price_per_month, bins=hist_range, histtype='bar', ec='black')
plt.grid(axis='y', alpha=0.5)
plt.suptitle("HDB RESALE PRICE in {} \n between Year {} to {}".format(town_selected, years.min(), years.max()), fontsize=14, fontweight='bold')
plt.title("Price per month from purchase date until End of Lease (usually 99 years)")
plt.xlabel("Price per month (SGD)")
plt.ylabel("Total Transaction")
plt.xticks(hist_range)
plt.show()
