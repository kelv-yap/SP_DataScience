import numpy as np

arr_2 = np.random.randint(1, 20, (3, 5))
print("**Before sorting**")
print(arr_2)
print()

arr_2.sort(axis=0)

print("**After sorting**")
print(arr_2)
