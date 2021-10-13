def sumf(n):            #Defining function to find sum
    if n == 1:          #Checking if number of terms is 1
        return 0        
    elif n == 2:        #Checking if number of terms is 2
        return 1
    else:
        a,b,sum=0,1,1   #Initializing 1st and 2nd terms and sum variable
        for i in range(2,n):
            c = a + b
            a, b = b, c
            sum = sum + c #Finding sum of all terms
        return sum
num = int(input("Enter number of terms:"))  #Inputs number of terms
#Printing the sum by calling the function
print(f"Sum of first {num} fibonacci numbers is {sumf(num)}") 