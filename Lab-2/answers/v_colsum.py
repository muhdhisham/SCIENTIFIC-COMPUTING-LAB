y =[[-4,-3,-2],                      #Initializing MATRIX-y
    [ 0, 2, 1],
    [ 1, 4, 2]]
r = [0,0,0]
for i in range(len(y)):              #Iterating through row of the matrix
    sum = 0
    for j in range(len(y[0])):       #Iterating through column of the matrix
        r[i] = r[i] + y[j][i]        #Finding sum of each column
print('\n',r)                        #Printing new 1-D matrix