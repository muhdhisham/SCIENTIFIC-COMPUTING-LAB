r = int(input("Enter real part:"))              #Input real part
i = int(input("Enter imaginary part:"))         #Input imaginary part
z = complex(r, i)                               #Converting into complex number
print(f"Complex number is {z}")                 #Printing the complex number
print(f"Absolute value of {z} is {abs(z)}")     #Printing absolute value of complex number
print(f"Real part of complex number is {z.real}") #Printing real part of complex number
print(f"Imaginary part of complex number is {z.imag}")#Printing imaginary part of complex number

