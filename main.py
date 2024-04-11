# Finding the Range of NumPy Array elements in Python

import numpy as np

arr = np.array([
    [5, 1, 10],
    [3, 2, 6],
    [8, 2, 4],
    [5, 10, 1]
])

row_range = np.ptp(arr, axis=1)
print(row_range)  # 👉️ [9 4 6 9]

column_range = np.ptp(arr, axis=0)
print(column_range)  # 👉️ [5 9 9]
