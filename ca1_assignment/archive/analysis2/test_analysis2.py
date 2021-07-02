import numpy as np
import matplotlib.pyplot as plt
import math


def calculate_price_per_month(purchase_year, lease_year, resale_price):
    lease = 99
    lease_remaining_year = lease_year + lease - purchase_year
    lease_remaining_month = lease_remaining_year * 12
    price_per_month = np.round(resale_price / lease_remaining_month, 2)
    return price_per_month


def calculate_histogram_range(min_value, max_value):
    hist_floor = int(math.floor(min_value / 100.0)) * 100
    hist_ceiling = int(math.ceil(max_value / 100.0)) * 100
    hist_range = np.arange(hist_floor, hist_ceiling+1, 100)
    return hist_range


# gaussian_numbers = np.random.randint(300, 1000, 1000)
# plt.hist(gaussian_numbers, bins=6)
#
# plt.title("Gaussian Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
#
# plt.show()




data = np.array([[2012,1986,250000],
                 [2012,1980,265000],
                 [2012,1980,315000],
                 [2012,1984,320000],
                 [2012,1980,321000],
                 [2012,1981,321000]])
print(np.shape(data))

plot_data = calculate_price_per_month(data[:,0], data[:,1], data[:,2])
print(plot_data)

minV = plot_data.min()
minM = plot_data.max()
print("minV: {}".format(minV))
print("minM: {}".format(minM))

# x_min, x_max, x_bin = calculate_histogram_range(minV, minM)
# print("x_min: {}".format(x_min))
# print("x_max: {}".format(x_max))
# print("x_bin: {}".format(x_bin))

hist_range = calculate_histogram_range(minV, minM)
print("hist_range: {}".format(hist_range))


# plt.figure(figsize=[10,8])
# n, bins, patches = plt.hist(x=plot_data, range=(x_min, x_max), bins=x_bin, color='#0504aa', alpha=1, histtype='bar', ec='black')
# plt.hist(x=plot_data, range=(x_min, x_max), bins=x_bin, color='#0504aa', alpha=1, histtype='bar', ec='black')
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('Value', fontsize=15)
# plt.ylabel('Frequency', fontsize=15)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.ylabel('Frequency', fontsize=15)
# plt.title('Histogram', fontsize=15)
# plt.show()









# plt.hist(plot_data, range=(x_min, x_max), bins=x_bin)
plt.hist(plot_data, bins=hist_range)

plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.xticks(hist_range)

plt.show()

