# Program to find the maximum number between two numbers

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if a>b:
    print(f"{a} is greater than {b}")
else:
    if a==b:
        print("Enter two unique numbers!")
    else:
        print(f"{b} is greater than {a}")