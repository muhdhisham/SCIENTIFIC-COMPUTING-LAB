y =[[-4,-3,-2],                      #Initializing MATRIX-y
    [ 0, 2, 1],
    [ 1, 4, 2]]
for i in range(1):                   #Iterating through row of the matrix
    for j in range(len(y[0])):       #Iterating through column of matrix
        y[i][j] = y [i][j] + 2       #Adding two to each element of 1st row

print("MATRIX-y after addition:")    #Printing the resultant
for i in y:
    print(i)