from matplotlib.lines import Line2D
import numpy as np
import matplotlib.pyplot as plt

csv_data = np.genfromtxt("data/hdb-carpark-information.csv",
                         delimiter=",",
                         usecols=(2, 3, 4, 5),
                         dtype=[('x_coord', 'f8'),
                                ('y_coord', 'f8'),
                                ('car_park_type', 'U30'),
                                ('type_of_parking_system', 'U30')])

data_coupon = csv_data[np.isin(csv_data['type_of_parking_system'], ['COUPON PARKING'])]
data_electric = csv_data[np.isin(csv_data['type_of_parking_system'], ['ELECTRONIC PARKING'])]

singapore_img = plt.imread('sg_map.png')
plt.imshow(singapore_img, extent=[919.05, 54338.72, 12576.34, 50172.05], alpha=0.5)
plt.suptitle('HDB CARPARK', fontsize=14, fontweight='bold')
plt.title('Location of Different Type of Parking Singapore')
plt.ylabel("Latitude", fontsize=10)
plt.xlabel("Longitude", fontsize=10)
plt.ylim(12576.34, 50172.05)
plt.xlim(919.05, 54338.72)
legend_elements = [Line2D([0], [0], marker='X', color='w', label='Coupon', markerfacecolor='r', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Electronic', markerfacecolor='b', markersize=10)]
plt.legend(handles=legend_elements, loc='upper left', title='Type of Parking')

plt.scatter(data_coupon['x_coord'], data_coupon['y_coord'], marker='x', color='red', alpha=0.5)
plt.scatter(data_electric['x_coord'], data_electric['y_coord'], marker='.', color='blue', alpha=0.5)

plt.show()
