x =[[0,1,2],            #Initializing MATRIX-1
    [3,4,5],
    [6,7,8]]
y =[[-4,-3,-2],         #Initializing MATRIX-2
    [0, 2, 1 ],
    [1, 4, 2 ]]
sum=[[0,0,0],           #Iitializing SUM MATRIX
     [0,0,0],
     [0,0,0]]
for i in range(len(x)):                 #Iterating through row of the matrix
    for j in range(len(x[0])):          #Iterating through column of matrix
        sum[i][j] = x[i][j] + y [i][j]  #Finding sum and storing result into another matrix
print("Sum of the matrices:")
for s in sum:                           #Printing the sum matrix
    print(s)
    