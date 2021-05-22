import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.full((3, 3), 1.5)
c = np.arange(0, 15).reshape(5, 3)

print("** Array a **")
print(a)
print()
print("** Array b **")
print(b)
print()
print("** Array c **")
print(c)
print()

d = np.concatenate((a, b, c), axis=0)
print("** Array after concatenate **")
print(d)
