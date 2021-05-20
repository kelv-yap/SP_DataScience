import numpy as np

a = np.array((np.arange(0, 10),
             np.arange(10, 20),
             np.arange(20, 30),
             np.arange(30, 40)))
print("Contents of array a")
print(a)
print()

print("*** Sum of all numbers in a ***")
print(np.sum(a))
print()

print("*** Mean of all numbers in a ***")
print(np.mean(a))
print()

print("*** Sum of all numbers in each row ***")
row_num = 1
for i in a:
    print("Row {} sum = {}".format(row_num, np.sum(i)))
    row_num += 1
