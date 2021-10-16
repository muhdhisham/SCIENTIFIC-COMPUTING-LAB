import numpy as np
x=np.array([[1,2,3],[3,2,1],[1,0,-1]])
y=np.array([[-4,-3,2],[1,2,1],[2,4,2]])
eix=np.linalg.eig(x)
print(eix[0])