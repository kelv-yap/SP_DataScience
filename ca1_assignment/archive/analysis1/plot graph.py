import numpy as np
import matplotlib.pyplot as plt


years = np.array(np.arange(2000, 2010))
print(years)

data = np.array([
    [1000, 2000, 3000, 5000, 1000, 1000, 2000, 3000, 4000, 5000],
    [1000, 2000, 2000, 4000, 5000, 1000, 2000, 5000, 4000, 5000],
    [1000, 2000, 3000, 4000, 2000, 1000, 2000, 3000, 2000, 5000]
])

# data_x = np.array([1000, 2000, 3000, 5000, 1000, 1000, 2000, 3000, 4000, 5000])
# data_y = np.array([1000, 2000, 2000, 4000, 5000, 1000, 2000, 5000, 4000, 5000])
# data_z = np.array([1000, 2000, 3000, 4000, 2000, 1000, 2000, 3000, 2000, 5000])

print(data)

# print(data_x)
# print(data_y)
# print(data_z)


# y = data[1]
# x_label = data[0]
# plt.xticks(np.arange(len(x_label)), x_label)
# plt.plot(y)

# plt.plot(data, labels)
# plt.ylabel('$psm', labelpad=20, fontsize=20)
# plt.xlabel('Year', labelpad=20, fontsize=20)
# plt.show()

plt.xticks(np.arange(len(years)),years)
plt.ylim(0,10000)

for i in data:
    plt.plot(i)

plt.show()


