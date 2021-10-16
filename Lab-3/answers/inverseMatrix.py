import numpy as np
a=np.array([[1,3,3],[1,4,3],[1,3,4]]).reshape(3,3)
b=np.linalg.inv(a)
print(b)