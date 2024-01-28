#description: This program takes the height and base of a triangle as inputs from the user, and prints the hypotenuse of the triangle.
#author: Max Hildebrand
#date: 1/25/2023

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
hypotenuse = ((base**2) + (height**2))**0.5
hypotenuse = round(hypotenuse, 2)
print("The hypotenuse is " + str(hypotenuse))
