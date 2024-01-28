#description: This program takes in a decimal number from the user and gives them the same value in binary and hexadecimal.
#author: Max Hildebrand
#date: 1/25/2023

print("This program converts a decimal positive integer to both binary and hexadecimal.")
numdec = int(input("Enter a positive integer: "))
numbin = bin(numdec)
numhex = hex(numdec)
print("The decimal value of " + str(numdec) + " is:")
print(str(numbin) + " in binary")
print(str(numhex) + " in hexadecimal")
