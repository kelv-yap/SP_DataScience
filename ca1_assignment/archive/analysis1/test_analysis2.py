import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


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
data4 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv", skiprows=1, delimiter=",", dtype=str)
data5 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv", skiprows=1, delimiter=",", dtype=str)

# print(len(data1))
# print(len(data2))
# print(len(data3))
# print(len(data4))
# print(len(data5))
# data_sum = len(data1) + len(data2) + len(data3) + len(data4) + len(data5)
# print("SUM: " + str(data_sum))

data = np.concatenate((data4, data5), axis=0)
# data = data5

print("Data4: {}".format(len(data4)))
print("Data5: {}".format(len(data5)))
del data4, data5


# del data3
# del data4
# del data5



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
# print(clean_data)
#
# town_list = np.unique(clean_data['town'])
# print(town_list)
#
