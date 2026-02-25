# Simple Calculator
# Created as a beginner Python practice project

print("***Simple Calculator***")

num1 = float(input("Enter the First Number:"))
num2 = float(input("Enter the Second Number:"))

print("Choose the Operation:")
print("a) Add")
print("b) Subtract")
print("c) Multipy")
print("d) Divide")

choice = input("Enter your choice (a,b,c,d):")

if choice == "a":
    print("Result = ", num1 + num2)
elif choice == "b":
    print("Result = ", num1 - num2)
elif choice == "c":
    print("Result = ", num1 * num2)
elif choice == "d":
    if num2 != 0:
        print("Result = ", num1 / num2)
    else:
        print("Can't Divide by 0")
else:
    print("Invalid Choice!")