# Program to find the area of triangle
# we use herons formula to find the area of triangle for 3 sides.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5 #Herons formula

print(f"Area of the Triangle is {area}")