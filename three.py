
"""

#take input from user and calulate the area of a circle
import math 
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2    
print("The area of the circle is: ", area)

#take input from user and calulate the area of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is: ", area)


#take input from user and calulate the area of a triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is: ", area)

#take input from user and calulate the area of a square
side = float(input("Enter the side of the square: "))
area = side ** 2
print("The area of the square is: ", area)

"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello, I am  " + name + " and I am " + str(age) + " years old.")