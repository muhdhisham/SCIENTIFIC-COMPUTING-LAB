import numpy as np
A = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])
b = np.array([4, 5, 6])
x = np.linalg.solve(A, b)
print(x)
