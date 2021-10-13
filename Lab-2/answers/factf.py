def fact(n):                    #Function to find factorial
    if n==1 or n==0:            #Since factorial of 1 and 0 is 1
        return 1
    else:                   
        return n * fact(n-1)    #Computing factorial through reccursion

num = int(input("Enter a number:"))         #Input a number
print(f"Factorial of {num} is {fact(num)}") #Printing the result
