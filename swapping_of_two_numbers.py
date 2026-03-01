#Swapping of two numbers

a = int(input("Enter the 1st value:"))
b = int(input("Enter the 2st value:"))

a = a+b
b = a-b
a = a-b

print(f"The value of A is {a} and value of B is {b}")