x =[[0,1,2],            #Initializing MATRIX-1
    [3,4,5],
    [6,7,8]]
y =[[-4,-3,-2],         #Initializing MATRIX-2
    [ 0, 2, 1],
    [ 1, 4, 2]]
pro=[[0,0,0],           #Iitializing Resultant MATRIX
    [0,0,0],
    [0,0,0]]
for i in range(len(x)):                 #Iterating through row of the matrix
    for j in range(len(x[0])):          #Iterating through column of matrix
        pro[i][j] = x[i][j] * y [i][j]  #Finding product and storing result into another matrix
print("Element vise product of the matrices:")
for p in pro:                           #Printing the Resultant matrix
    print(p)