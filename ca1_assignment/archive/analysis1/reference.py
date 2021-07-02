import numpy as np
import matplotlib.pyplot as plt


def addRegionColumn(town):
    # print(town)
    a = []
    # print(np.unique(town))
    for i in town:
        # x = np.asarray(i)
        # print("Looping: {}".format(x))
        # print(x[1])
        a.append(regionMapper(i))
        # reg = regionMapper(x[1])
        # print("Region: {}".format(reg))
        # # print(np.array(i))
        # c = np.insert(x, np.shape(x)[2], reg, axis=1)
        # print(c)
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

def calculatePricePerSquareMeter(data):
    a = []
    for i in data:
        x = float(i[5])
        y = float(i[3])
        a.append(int(x / y))
    return a

# data1 = np.loadtxt("data/resale-flat-prices-based-on-approval-date-1990-1999.csv", skiprows=1, delimiter=",", dtype=str)
# data2 = np.loadtxt("data/resale-flat-prices-based-on-approval-date-2000-feb-2012.csv", skiprows=1, delimiter=",", dtype=str)
# data3 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv", skiprows=1, delimiter=",", dtype=str)
# data5 = np.loadtxt("data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv", skiprows=1, delimiter=",", dtype=str)
data = np.loadtxt("data/dummy.csv",
                  skiprows=1,
                  delimiter=",",
                  # dtype=[('month', 'U10'),
                  #        ('town', 'U30'),
                  #        ('flat_type', 'U30'),
                  #        ('floor_area_sqm', 'U30'),
                  #        ('lease_commence_date', 'U30'),
                  #        ('resale_price', 'U30')]
                  dtype=str
                  )


print("Original Data counts: {}".format(len(data)))


region = addRegionColumn(data[:, 1])
print(region)
data = np.insert(data, np.shape(data)[1], region, axis=1)

# psm = calculatePricePerSquareMeter(data)
# # print(psm)
# data = np.insert(data, np.shape(data)[1], psm, axis=1)


print("Amended Data counts: {}".format(len(data)))
print(data)

# np.savetxt("data/clean_data.csv", data, delimiter=",")


# data_east = data[np.isin(data['town'], ['PUNGGOL'])]['resale_price']
# print(data_east)










# ori_date_col = data[:, 0]
# print("Original Date column: {}".format(ori_date_col))
# amended_date_col = np.array(ori_date_col, dtype='datetime64')
# print("Amended Date column: {}".format(amended_date_col))
# for i in len(ori_date_col):
#     print(np.datetime64(i, 'Y'))

# print(data)







print("Shape: " + str(clean_data.shape))
print("Dimension: " + str(clean_data.ndim))

a = np.array(np.asarray(clean_data))
print("a Shape: " + str(a.shape))

b = np.array([
    [1,2],
    [3,4],
    [5,6]
])
print("b Shape: "+str(b.shape))



c = np.array(
[['2015', 'ANG MO KIO', '3 ROOM',  60, '1986', 255000, 'NORTH-EAST'],
 ['2015', 'ANG MO KIO', '3 ROOM',  68, '1981', 275000, 'NORTH-EAST'],
 ['2015', 'ANG MO KIO', '3 ROOM',  69, '1980', 285000, 'NORTH-EAST'],
 ['2015', 'ANG MO KIO', '3 ROOM',  68, '1979', 290000, 'NORTH-EAST']
])
print("c Shape: "+str(c.shape))




# fig = plt.figure()
# fig.suptitle('XXXX', fontsize=14, fontweight='bold')
# ax = fig.add_subplot(111)
# fig.subplots_adjust(top=0.85)
# ax.set_title('Average Resale Price per Square Meter by Region')
# ax.set_xlabel('Year')
# ax.set_ylabel('Price (psm)')


# plt.xticks(np.arange(10), years)
# plt.xticks(np.arange(2017, 2021, 2), years)
# plt.xlim(np.arange(len(years)),years)
# plt.ylim(0, 7000)
# plt.axis(1990, 2020, 0, 7000)
# plt.xticks(np.arange(1990, 2022, 5))


# data = data[np.isin(data['flat_type'], ['2 ROOM']) or
#             np.isin(data['flat_type'], ['3 ROOM']) or
#             np.isin(data['flat_type'], ['4 ROOM']) or
#             np.isin(data['flat_type'], ['5 ROOM']) or
#             np.isin(data['flat_type'], ['EXECUTIVE'])]


def addRegionColumn(town):
    a = []
    for i in town:
        a.append(regionMapper(i))
    return a
# region = addRegionColumn(data[:, 1])















data = np.genfromtxt("data/hdb-carpark-information.csv",
                           delimiter=",",
                            usecols=(2,3,4,5),
                           dtype=[('x_coord', 'f8'),
                                  ('y_coord', 'f8'),
                                  ('car_park_type', 'U30'),
                                  ('type_of_parking_system', 'U30')]
                           )

# print(data)

data_coupon = data[np.isin(data['type_of_parking_system'], ['COUPON PARKING'])]
# data_outdoor = data[np.isin(data['car_park_type'], ['SURFACE CAR PARK']) |
#                     np.isin(data['car_park_type'], ['MECHANISED AND SURFACE CAR PARK']) |
#                     np.isin(data['car_park_type'], ['SURFACE/MULTI-STOREY CAR PARK'])]
data_electric = data[np.isin(data['type_of_parking_system'], ['ELECTRONIC PARKING'])]
# print(filtered_data)

# print(len(data_outdoor))

# print(len(filtered_data['x_coord']))
# print(len(filtered_data['y_coord']))

# print(data['car_park_type'])


# data_outdoor = []
# for i in data:
#     if 'SURFACE' in i['car_park_type']:
#         data_outdoor.append(i)
# print(len(data_outdoor))
# print(data_outdoor)





# data_outdoor = data[any('SURFACE CAR PARK' in x for x in data['car_park_type'])]
# print(len(data_outdoor))




# count = 0
# if any('SURFACE' in x for x in data['car_park_type']):
#     count += 1


# matching = np.unique([s for s in data['car_park_type'] if "SURFACE" in s])
# print(matching)
# print(len(matching))

# print("COUNT: {}".format(count))

# print(len(data_coupon))
# print(len(data_outdoor))





# plot_data = np.array([filtered_data['x_coord'], filtered_data['y_coord']])
# print(plot_data)

singapore_img = plt.imread('sgmap.png')

# use our map with it's bounding coordinates
plt.imshow(singapore_img, extent=[919.05, 54338.72, 12576.34, 50172.05], alpha=0.5)


# plt.scatter([30314.7936, 33758.4143, 29257.7203, 28185.4359],
#             [31490.4942, 33695.5198, 34500.3599, 39012.6664], marker='^')
#
# plt.scatter([25000.7936, 26000.4143, 27000.7203, 28000.4359],
#             [30000.4942, 31000.5198, 32000.3599, 33000.6664], marker='^')

plt.scatter(data_coupon['x_coord'], data_coupon['y_coord'], marker='x', color='red', alpha=0.7)
plt.scatter(data_electric['x_coord'], data_electric['y_coord'], marker='.', color='blue', alpha=0.7)

plt.ylabel("Latitude", fontsize=10)
plt.xlabel("Longitude", fontsize=10)
plt.ylim(12576.34, 50172.05)
plt.xlim(919.05, 54338.72)
plt.show()


