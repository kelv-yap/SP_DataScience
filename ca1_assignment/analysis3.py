from matplotlib.lines import Line2D
import numpy as np
import matplotlib.pyplot as plt


def calculate_parking_system_distribution(coupon_count, electronic_count):
    total_count = coupon_count + electronic_count
    coupon_percentage = np.round((coupon_count / total_count) * 100, 2)
    electronic_percentage = np.round((electronic_count / total_count) * 100, 2)
    return coupon_percentage, electronic_percentage


csv_data = np.genfromtxt("data/hdb-carpark-information.csv",
                         delimiter=",",
                         usecols=(2, 3, 4, 5),
                         dtype=[('x_coord', 'f8'),
                                ('y_coord', 'f8'),
                                ('car_park_type', 'U30'),
                                ('type_of_parking_system', 'U30')])

data_coupon = csv_data[np.isin(csv_data['type_of_parking_system'], ['COUPON PARKING'])]
data_electronic = csv_data[np.isin(csv_data['type_of_parking_system'], ['ELECTRONIC PARKING'])]
perc_coupon, perc_electronic = calculate_parking_system_distribution(len(data_coupon), len(data_electronic))

singapore_img = plt.imread('data/sg_map.png')
plt.imshow(singapore_img, extent=[919.05, 54338.72, 12576.34, 50172.05], alpha=0.5)
plt.suptitle("HDB CARPARK", fontsize=14, fontweight='bold')
plt.title("Type of Parking System in HDB")
legend_elements = [Line2D([0], [0], marker='X', color='w', label="Coupon ({}%)".format(perc_coupon), markerfacecolor='r', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label="Electronic ({}%)".format(perc_electronic), markerfacecolor='b', markersize=10)]
plt.legend(handles=legend_elements, loc='upper left', title='Type of Parking')
plt.axis('off')

plt.scatter(data_coupon['x_coord'], data_coupon['y_coord'], marker='x', color='red', alpha=0.6)
plt.scatter(data_electronic['x_coord'], data_electronic['y_coord'], marker='.', color='blue', alpha=0.6)

plt.show()
