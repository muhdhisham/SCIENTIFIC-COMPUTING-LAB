import numpy as np
A = np.array([[2, 0, 8, 6, 0], [1, 6, 0, 1, 7], [5, 0, 7, 4, 0], [7, 0, 8, 5, 0], [0, 10, 0, 0,7]])
u, s, v = np.linalg.svd(A)
print("left singular matrix")
print(u)
print("right singular matrix")
print(v)
print("matrix with eigen values")
print(s) 