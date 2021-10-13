import numpy as np
x = np.array([  [0,1,2],            #Initializing MATRIX-1
                [3,4,5],
                [6,7,8]])
y = np.array([  [-4,-3,-2],         #Initializing MATRIX-2
                [ 0, 2, 1],
                [ 1, 4, 2]])
#Printing the product
print("Element vise product of the matrices:\n",np.multiply(x,y))