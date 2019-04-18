import numpy as np

a = np.zeros((2, 2), dtype=np.int)

a[0][0] = 1
a[0][1] = 2
a[1][0] = 3
a[1][1] = 4

print(a)
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
for i in range(1, 14):
	print(i)
