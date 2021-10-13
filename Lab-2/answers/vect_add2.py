import numpy as np
y = np.array(  [[-4,-3,-2],         #Initializing MATRIX-y
                [ 0, 2, 1],
                [ 1, 4, 2]])
y[0] = y[0] + 2                     #Adding 2 to elements in 1st row
print("Matrix after adding 2 in first row:")    #Printing final matrix
for i in y:
    print(i)                        #Printing resultant matrix