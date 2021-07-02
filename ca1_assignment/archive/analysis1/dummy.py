import numpy as np
import matplotlib.pyplot as plt


# data = np.array([
#         ["1990", 1234],
#         ["1991", 1234],
#         ["1992", 1234],
#         ["1993", 1234],
#         ["1994", 1234],
#         ["1995", 1234],
#         ["1996", 1234],
#         ["1997", 1234],
#         ["1998", 1234],
#         ["1999", 1234]
#     ])

data = np.array([
    [1990, 1991, 1992, 1993],
    [1000, 2000, 3000, 4000]
])

print(data)

# plt.plot(
#     ['1990', '1991', '1992', '1993'],
#     [1234, 1234, 1234, 1234]
# )
# plt.plot(data)


y = data[1]
x_label = data[0]
plt.xticks(np.arange(len(x_label)), x_label)
plt.plot(y)
plt.show()


