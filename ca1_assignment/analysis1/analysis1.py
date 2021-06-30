import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

town_list = [
    "ANG MO KIO",
    "BEDOK",
    "BISHAN",
    "BUKIT BATOK",
    "BUKIT MERAH",
    "BUKIT PANJANG",
    "BUKIT TIMAH",
    "CENTRAL AREA",
    "CHOA CHU KANG",
    "CLEMENTI",
    "GEYLANG",
    "HOUGANG",
    "JURONG EAST",
    "JURONG WEST",
    "KALLANG/WHAMPOA",
    "LIM CHU KANG",
    "MARINE PARADE",
    "PASIR RIS",
    "PUNGGOL",
    "QUEENSTOWN",
    "SEMBAWANG",
    "SENGKANG",
    "SERANGOON",
    "TAMPINES",
    "TOA PAYOH",
    "WOODLANDS",
    "YISHUN"]

# else:
#     print("{} ${:.2f} added!".format(*town_list[index]))
#     quantity = int(input("How many {} do you want to order?: ".format(town_list[index][0])))
#     total_cost = float(town_list[index][1]) * quantity
#     print("The total cost for {} {} is ${:.2f}".format(quantity, town_list[index][0], total_cost))




def regionMapper(town):
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


# data1 = np.loadtxt("data/resale-flat-prices-based-on-approval-date-1990-1999.csv", skiprows=1, delimiter=",", dtype=str)
# data2 = np.loadtxt("data/resale-flat-prices-based-on-approval-date-2000-feb-2012.csv", skiprows=1, delimiter=",", dtype=str)
# data3 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv", skiprows=1, delimiter=",", dtype=str)
# data4 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv", skiprows=1, delimiter=",", dtype=str)
data5 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv", skiprows=1, delimiter=",", dtype=str)

# print(len(data1))
# print(len(data2))
# print(len(data3))
# print(len(data4))
# print(len(data5))
# data_sum = len(data1) + len(data2) + len(data3) + len(data4) + len(data5)
# print("SUM: " + str(data_sum))

# data = np.concatenate((data1, data2, data3, data4, data5), axis=0)
data = data5

print("Original Data counts: {}".format(len(data)))

# Create column Region
region = []
for i in data[:, 1]:
    region.append(regionMapper(i))
data = np.insert(data, np.shape(data)[1], region, axis=1)

print("Amended Data counts: {}".format(len(data)))

np.savetxt("data/clean_data.csv",
           data,
           delimiter=",",
           fmt=['%s', '%s', '%s', '%s', '%s', '%s', '%s'],
           header='purchase_year, town, flat_type, floor_area_sqm, lease_commence_year, resale_price, region')


clean_data = np.loadtxt("data/clean_data.csv",
                        skiprows=1,
                        delimiter=",",
                        # usecols=(0,3,5,6),
                        dtype=[('purchase_year', 'U10'),
                               ('town', 'U30'),
                               ('flat_type', 'U30'),
                               ('floor_area_sqm', 'i4'),
                               ('lease_commence_year', 'U10'),
                               ('resale_price', 'i4'),
                               ('region', 'U30')]
                        # dtype=str
                        )

# ======================
# DATASET: 1
# GRAPH: 1 (LINE CHART)
# ======================

# Transform yyyy-mm to yyyy
clean_data['purchase_year'] = [datetime.strptime(date, '%Y-%m').year for date in clean_data['purchase_year']]
years = np.unique(clean_data['purchase_year'])
years = np.array(sorted(years))

region = np.unique(clean_data['region'])
region = np.array(sorted(region))

plot_data = []
print("============ START LOOPING ===========")
for j in region:
    data_region = []
    for i in years:
        x = clean_data[np.isin(clean_data['region'], [j]) &
                       np.isin(clean_data['purchase_year'], [i])]

        has_elements = x.size > 0
        if has_elements:
            price = x['resale_price']
            sm = x['floor_area_sqm']
            # psm = np.round(price / sm, 2)
            # print("PSM: {}".format(psm))
            # data_region.append(int(psm.mean()))

            sqft = np.round(sm * 10.7639)
            psqft = np.round(price / sqft, 2)
            data_region.append(int(psqft.mean()))

        else:
            data_region.append(0)

    plot_data.append(data_region)

print("============ STOP LOOPING ===========")
print(plot_data)

# Graph 1: Line Graph (Cosmetic)
color = ['orange', 'green', 'red', 'purple', 'black']
plt.suptitle('HDB RESALE PRICE', fontsize=14, fontweight='bold')
plt.title('Average Resale Price per Square Feet (sqft) by Region')
plt.xlabel('Year')
plt.ylabel('Price (per sqft)')
plt.xticks(np.arange(len(years)),years)
plt.yticks(np.arange(0, 700, 100))

count = 0
for i in plot_data:
    plt.plot(i, label=region[count], color=color[count])
    count = count+1
legend = plt.legend(loc='upper left', shadow=True)
plt.show()


# ======================
# DATASET: 1
# GRAPH: 2 (BOXPLOT)
# ======================
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

data_filtered_by_flat_type = clean_data[np.isin(clean_data['flat_type'], ['2 ROOM']) |
                                        np.isin(clean_data['flat_type'], ['3 ROOM']) |
                                        np.isin(clean_data['flat_type'], ['4 ROOM']) |
                                        np.isin(clean_data['flat_type'], ['5 ROOM']) |
                                        np.isin(clean_data['flat_type'], ['EXECUTIVE'])]
hdb_type = np.unique(data_filtered_by_flat_type['flat_type'])
hdb_type = np.array(sorted(hdb_type))
print(hdb_type)

x_label = []
data_byRoomType = []
print("============ START LOOPING ===========")
for typ in hdb_type:
    x = data_filtered_by_flat_type[np.isin(data_filtered_by_flat_type['flat_type'], [typ]) &
                                   np.isin(data_filtered_by_flat_type['town'], [town_selected])]

    has_elements = x.size > 0
    if has_elements:
        x_label.append(typ)
        price = x['resale_price']
        sm = x['floor_area_sqm']
        sqft = np.round(sm * 10.7639)
        psqft = np.round(price / sqft, 2)
        data_byRoomType.append(psqft)

print("============ STOP LOOPING ===========")
# print(x_label)
# print(data_byRoomType)

# Graph 2: Boxplot (Cosmetic)
plt.suptitle('HDB RESALE PRICE in {}'.format(town_selected), fontsize=14, fontweight='bold')
plt.title('Average Resale Price per Square Feet (sqft) by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Price (per sqft)')

plt.boxplot(data_byRoomType, labels=x_label)
plt.show()


