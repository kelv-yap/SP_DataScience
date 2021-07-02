from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np

# legend_elements = [Line2D([0], [0], marker='X', color='w', label='Coupon', markerfacecolor='r', markersize=15),
#                    Line2D([0], [0], marker='o', color='w', label='Electronic', markerfacecolor='b', markersize=15)
#                    ]
#
# fig, ax = plt.subplots()
# ax.legend(handles=legend_elements, loc='center right')
#
# plt.show()


teams = np.arange(3)
scores = (20, 35, 30)
width = 0.35
p1t = plt.bar(teams, scores, width, color='#d62728')

plt.ylabel('Scores')
plt.title('Scores by Team')
plt.xticks(teams, ('Team 1', 'Team 2', 'Team 3'))
plt.yticks(np.arange(0, 50, 10))

plt.show()
