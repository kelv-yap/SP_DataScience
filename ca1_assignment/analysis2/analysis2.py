from datetime import datetime
import os
import numpy as np
import matplotlib.pyplot as plt


def calculate_price_per_square_feet(resale_price, square_meter_area):
    convert_sm_to_sqft = 10.7639
    square_feet_area = np.round(square_meter_area * convert_sm_to_sqft)
    per_sqft = np.round(resale_price / square_feet_area, 2)
    return per_sqft


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

# Save transformed data to new file
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
# DATASET: 2
# GRAPH: 1 (BOXPLOT)
# ======================
filtered_data_by_flat_type = saved_data[np.isin(saved_data['flat_type'], ['2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE'])]
hdb_type = np.unique(filtered_data_by_flat_type['flat_type'])

x_label = []
data_by_room_type = []

for type in hdb_type:
    filtered_data = filtered_data_by_flat_type[np.isin(filtered_data_by_flat_type['flat_type'], [type]) &
                                               np.isin(filtered_data_by_flat_type['town'], [town_selected])]

    has_elements = filtered_data.size > 0
    if has_elements:
        x_label.append(type)
        resale_price = filtered_data['resale_price']
        square_meter_area = filtered_data['floor_area_sqm']
        per_sqft = calculate_price_per_square_feet(resale_price, square_meter_area)
        data_by_room_type.append(per_sqft)

# Graph 2: Boxplot (Cosmetic)
plt.suptitle('HDB RESALE PRICE in {}'.format(town_selected), fontsize=14, fontweight='bold')
plt.title('Average Resale Price per Square Feet (sqft) by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Price (per sqft)')

plt.boxplot(data_by_room_type, labels=x_label)
plt.show()



# ======================
# DATASET: 2
# GRAPH: 2 (BAR CHART)
# ======================
chart2_data = np.copy(saved_data)
print("COUNT SAVED DATA: {}".format(len(saved_data)))
print("COUNT CHART2 DATA: {}".format(len(chart2_data)))
chart2_data['purchase_date'] = [datetime.strptime(date, '%Y-%m').month for date in chart2_data['purchase_date']]

months = np.unique(chart2_data['purchase_date'])
# print(months)

print(town_selected)
# filtered_data_by_town_selected = chart2_data[np.isin(chart2_data['town'], [town_selected])]
# print("COUNT filtered_data_by_town_selected DATA: {}".format(len(filtered_data_by_town_selected)))
# print(filtered_data_by_town_selected)
# print(np.unique(filtered_data_by_town_selected['town']))

chart_2_x_label = []
data_total_purchase_by_month = []
for month in months:
    # filtered_data = filtered_data_by_town_selected[np.isin(filtered_data_by_town_selected['purchase_date'], [month])]
    filtered_data = chart2_data[np.isin(chart2_data['purchase_date'], [month])]
    print("For {} month: {}".format(month, len(filtered_data)))
    chart_2_x_label.append(month)
    data_total_purchase_by_month.append(len(filtered_data))

print(chart_2_x_label)
print(data_total_purchase_by_month)



# teams = np.arange(3)
# scores = (20, 35, 30)
width = 0.35
p1t = plt.bar(chart_2_x_label, data_total_purchase_by_month, width, color='#d62728')

# plt.ylabel('Scores')
# plt.title('Scores by Team')
# plt.xticks(chart_2_x_label, ('Team 1', 'Team 2', 'Team 3'))
plt.yticks(np.arange(0, 20000, 2000))





# Graph 2: Bar Chart (Cosmetic)
plt.suptitle('HDB RESALE TRANSACTIONS', fontsize=14, fontweight='bold')
plt.title('Total Resale Transaction by Month')
plt.xlabel('Month')
plt.ylabel('Total')

# plt = plt.bar(chart_2_x_label, data_total_purchase_by_month)
# plt.yticks(np.arange(data_total_purchase_by_month))

plt.show()









