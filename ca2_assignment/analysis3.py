from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calculate_parking_system_distribution(coupon_count, electronic_count):
    total_count = coupon_count + electronic_count
    coupon_percentage = np.round((coupon_count / total_count) * 100, 2)
    electronic_percentage = np.round((electronic_count / total_count) * 100, 2)
    return coupon_percentage, electronic_percentage


df = pd.read_csv('data/hdb-carpark-information.csv', sep=',',
                 usecols=['x_coord', 'y_coord', 'car_park_type', 'type_of_parking_system'])

data_coupon = df[df.type_of_parking_system.isin(['COUPON PARKING'])]
data_electronic = df[df.type_of_parking_system.isin(['ELECTRONIC PARKING'])]
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
