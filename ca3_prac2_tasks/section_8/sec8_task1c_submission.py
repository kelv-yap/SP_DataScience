import numpy as np

arr_3 = np.random.randint(100, 200, (2, 5))
arr_4 = np.copy(arr_3)
arr_4.sort()

print("**Before sorting - original array **")
print(arr_3)
print()
print("**After calling sort method - original array **")
print(arr_3)
print()
print("**After calling sort method - copy of sorted array **")
print(arr_4)
