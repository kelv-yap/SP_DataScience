import numpy as np

a = np.array((np.arange(0, 10),
             np.arange(10, 20),
             np.arange(20, 30),
             np.arange(30, 40)))
print("** Array a **")
print(a)

x = a % 2 == 0
a = a[x]
print("** Array a - even number **")
print(a)
print()

b = np.random.randint(100, 200, (3, 3))
print("** Array b **")
print(b)

y = b > 150
b = b[y]
print("** Array b - number greater than 150 **")
print(b)
