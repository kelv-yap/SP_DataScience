import numpy as np
import matplotlib.pyplot as plt


def addRegionColumn(town):
    a = []
    # print(np.unique(town))
    for i in town:
        a.append(regionMapper(i))
    return a


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


data1 = np.loadtxt("data/resale-flat-prices-based-on-approval-date-1990-1999.csv", skiprows=1, delimiter=",", dtype=str)
data2 = np.loadtxt("data/resale-flat-prices-based-on-approval-date-2000-feb-2012.csv", skiprows=1, delimiter=",", dtype=str)
data3 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv", skiprows=1, delimiter=",", dtype=str)
data4 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv", skiprows=1, delimiter=",", dtype=str)
data5 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv", skiprows=1, delimiter=",", dtype=str)

print(len(data1))
print(len(data2))
print(len(data3))
print(len(data4))
print(len(data5))
data_sum = len(data1) + len(data2) + len(data3) + len(data4) + len(data5)
print("SUM: " + str(data_sum))

data = np.concatenate((data1, data2, data3, data4, data5), axis=0)
# data = data5


print("Original Data counts: {}".format(len(data)))



# Convert Date to Year only
for i in data:
    i[0] = np.datetime64(i[0], 'Y')

# Create column Region
region = addRegionColumn(data[:, 1])
# print(region)
data = np.insert(data, np.shape(data)[1], region, axis=1)

# data = data[np.isin(data['flat_type'], ['2 ROOM']) or
#             np.isin(data['flat_type'], ['3 ROOM']) or
#             np.isin(data['flat_type'], ['4 ROOM']) or
#             np.isin(data['flat_type'], ['5 ROOM']) or
#             np.isin(data['flat_type'], ['EXECUTIVE'])]

print("Amended Data counts: {}".format(len(data)))
# print(data)

np.savetxt("data/clean_data.csv",
           data,
           delimiter=",",
           fmt=['%s', '%s', '%s', '%s', '%s', '%s', '%s'],
           header='purchase_year, town, flat_type, floor_area_sqm, lease_commence_year, resale_price, region')


clean_data = np.loadtxt("data/clean_data.csv",
                        skiprows=1,
                        delimiter=",",
                        usecols=(0,3,5,6),
                        dtype=[('purchase_year', 'U10'),
                               # ('town', 'U30'),
                               # ('flat_type', 'U30'),
                               ('floor_area_sqm', 'i4'),
                               # ('lease_commence_year', 'U10'),
                               ('resale_price', 'i4'),
                               ('region', 'U30')]
                        # dtype=str
                        )

years = np.unique(clean_data['purchase_year'])
years = np.array(sorted(years))
print(years)

region = np.unique(clean_data['region'])
region = np.array(sorted(region))
print(region)


plot_data = []
# data_y = []
print("============ START LOOPING ===========")
for j in region:

    # print("region: {}".format(j))
    # plot_data.append(j)

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

    # print(data_region)
    plot_data.append(data_region)

print("============ STOP LOOPING ===========")

print(plot_data)

plt.xticks(np.arange(len(years)),years)
# plt.xticks(np.arange(10), years)
# plt.xticks(np.arange(2017, 2021, 2), years)
# plt.xlim(np.arange(len(years)),years)
# plt.ylim(0, 7000)
# plt.axis(1990, 2020, 0, 7000)
# plt.xticks(np.arange(1990, 2022, 5))
plt.yticks(np.arange(0, 700, 100))

color = ['orange', 'green', 'red', 'purple', 'black']

# fig = plt.figure()
# fig.suptitle('XXXX', fontsize=14, fontweight='bold')
# ax = fig.add_subplot(111)
# fig.subplots_adjust(top=0.85)
# ax.set_title('Average Resale Price per Square Meter by Region')
# ax.set_xlabel('Year')
# ax.set_ylabel('Price (psm)')
plt.suptitle('HDB RESALE PRICE', fontsize=14, fontweight='bold')
plt.title('Average Resale Price per Square Feet (sqft) by Region')
plt.xlabel('Year')
plt.ylabel('Price (per sqft)')


count = 0
for i in plot_data:
    plt.plot(i, label=region[count], color=color[count])
    count = count+1

legend = plt.legend(loc='upper left', shadow=True)

plt.show()
