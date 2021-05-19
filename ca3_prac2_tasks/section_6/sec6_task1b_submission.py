import numpy as np

a = np.array([[1, 2, 3, 4],
              [4, 5, 6, 7],
              [7, 8, 9, 10],
              [11, 12, 13, 14]])
b = np.random.randint(100, 200, (4, 6))
c = np.arange(0, 40).reshape(4, 10)

print(a)
print(b)
print(c)
print()

d = np.concatenate((a, b, c), axis=1)

print(d)
