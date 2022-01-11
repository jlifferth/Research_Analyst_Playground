from dtw import dtw
import numpy as np
import pandas as pd

# We define two sequences x, y as numpy array
# where y is actually a sub-sequence from x
x = np.array([2, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
y = np.array([1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)

df = pd.read_csv('Links in tracks statistics.csv')
track_7 = df['TRACK_ID'] = 7
print(track_7)

manhattan_distance = lambda x, y: np.abs(x - y)

# d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=manhattan_distance)

# print(d)
# >>> 2.0 # Only the cost for the insertions is kept

# You can also visualise the accumulated cost and the shortest path
import matplotlib.pyplot as plt

# plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
# plt.plot(path[0], path[1], 'w')
# plt.show()
