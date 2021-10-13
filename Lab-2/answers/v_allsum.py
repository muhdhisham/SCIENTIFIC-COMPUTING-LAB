x =[[0,1,2],                                #Initializing MATRIX-x
    [3,4,5],
    [6,7,8]]
sum = 0
for i in range(len(x)):                     #Iterating through row of the matrix
    for j in range(len(x[0])):              #Iterating through column of matrix
        sum = x[i][j] + sum  
print("\nSum of Elements of Matrix is",sum)   #Printing Sum