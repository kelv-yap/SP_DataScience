from datetime import datetime
import os
import numpy as np
import matplotlib.pyplot as plt


def region_mapper(town):
    mapper = {
        "SEMBAWANG": "NORTH",
        "WOODLANDS": "NORTH",
        "YISHUN": "NORTH",
        "ANG MO KIO": "NORTH-EAST",
        "HOUGANG": "NORTH-EAST",
        "PUNGGOL": "NORTH-EAST",
        "SENGKANG": "NORTH-EAST",
        "SERANGOON": "NORTH-EAST",
        "BEDOK": "EAST",
        "PASIR RIS": "EAST",
        "TAMPINES": "EAST",
        "BUKIT BATOK": "WEST",
        "BUKIT PANJANG": "WEST",
        "CHOA CHU KANG": "WEST",
        "LIM CHU KANG": "WEST",
        "CLEMENTI": "WEST",
        "JURONG EAST": "WEST",
        "JURONG WEST": "WEST",
        "BISHAN": "CENTRAL",
        "BUKIT MERAH": "CENTRAL",
        "BUKIT TIMAH": "CENTRAL",
        "CENTRAL AREA": "CENTRAL",
        "GEYLANG": "CENTRAL",
        "KALLANG/WHAMPOA": "CENTRAL",
        "MARINE PARADE": "CENTRAL",
        "QUEENSTOWN": "CENTRAL",
        "TOA PAYOH": "CENTRAL"
    }
    return mapper.get(town, "Invalid Town")


def calculate_price_per_square_feet(resale_price, square_meter_area):
    convert_sm_to_sqft = 10.7639
    square_feet_area = np.round(square_meter_area * convert_sm_to_sqft)
    per_sqft = np.round(resale_price / square_feet_area, 2)
    return per_sqft


if os.path.exists('data/clean_data.csv'):
    os.remove("data/clean_data.csv")
csv_data1 = np.loadtxt("data/resale-flat-prices-based-on-approval-date-1990-1999.csv", skiprows=1, delimiter=",", dtype=str)
csv_data2 = np.loadtxt("data/resale-flat-prices-based-on-approval-date-2000-feb-2012.csv", skiprows=1, delimiter=",", dtype=str)
csv_data3 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv", skiprows=1, delimiter=",", dtype=str)
csv_data4 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv", skiprows=1, delimiter=",", dtype=str)
csv_data5 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv", skiprows=1, delimiter=",", dtype=str)

combined_data_count = len(csv_data1) + len(csv_data2) + len(csv_data3) + len(csv_data4) + len(csv_data5)
print("Data Count (Before Concatenate): " + str(combined_data_count))

combined_data = np.concatenate((csv_data1, csv_data2, csv_data3, csv_data4, csv_data5), axis=0)
del csv_data1, csv_data2, csv_data3, csv_data4, csv_data5
print("Data Count (Before Concatenate): {}".format(len(combined_data)))

# Create column Region
region = []
for i in combined_data[:, 1]:
    region.append(region_mapper(i))
combined_data = np.insert(combined_data, np.shape(combined_data)[1], region, axis=1)

# Save transformed data to new file
np.savetxt("data/clean_data.csv",
           combined_data,
           delimiter=",",
           fmt=['%s', '%s', '%s', '%s', '%s', '%s', '%s'],
           header='purchase_date, town, flat_type, floor_area_sqm, lease_commence_year, resale_price, region')
del combined_data

saved_data = np.genfromtxt("data/clean_data.csv",
                           delimiter=",",
                           dtype=[('purchase_date', 'U10'),
                                  ('town', 'U30'),
                                  ('flat_type', 'U30'),
                                  ('floor_area_sqm', 'i4'),
                                  ('lease_commence_year', 'U10'),
                                  ('resale_price', 'i4'),
                                  ('region', 'U30')]
                           )
print("Saved Data counts: {}".format(len(saved_data)))

chart1_data = np.copy(saved_data)
chart1_data['purchase_date'] = [datetime.strptime(date, '%Y-%m').year for date in chart1_data['purchase_date']]

years = np.unique(chart1_data['purchase_date'])
regions = np.unique(chart1_data['region'])

data_price_by_region = []
for region in regions:
    data_by_region = []
    for year in years:
        filtered_data = chart1_data[np.isin(chart1_data['region'], [region]) &
                                    np.isin(chart1_data['purchase_date'], [year])]

        has_elements = filtered_data.size > 0
        if has_elements:
            resale_price = filtered_data['resale_price']
            square_meter_area = filtered_data['floor_area_sqm']
            per_sqft = calculate_price_per_square_feet(resale_price, square_meter_area)
            data_by_region.append(int(per_sqft.mean()))
        else:
            data_by_region.append(0)

    data_price_by_region.append(data_by_region)

# Graph 1: Line Graph (Cosmetic)
color = ['orange', 'green', 'red', 'purple', 'black']
plt.grid(axis='x', alpha=0.5)
plt.grid(axis='y', alpha=0.5)
plt.suptitle('HDB RESALE PRICE', fontsize=14, fontweight='bold')
plt.title('Average Resale Price per Square Feet (sqft) by Region')
plt.xlabel('Year')
plt.ylabel('Price (per sqft)')
plt.xticks(np.arange(len(years)), years)
plt.yticks(np.arange(0, 700, 100))

count = 0
for i in data_price_by_region:
    plt.plot(i, label=regions[count], color=color[count])
    count += 1
legend = plt.legend(loc='upper left', shadow=True)
plt.show()
