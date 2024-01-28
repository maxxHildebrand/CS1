#This program gives you a number to a certain power
#Max Hildebrand
#2/20/2023

#power function

def power(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    elif power > 0:
        constant = base
        for counter in range(0, power - 1):
             base = base * constant
        return base
    elif power < 0:
        constant = base
        for counter in range(0, abs(power) - 1):
             base = base * constant
        return 1/base

#main code  

print("This program gives you a number to a certain power.")

baseinp = float(input("Enter the number: "))
powinp = int(input("Enter the power: "))

print()
print(power(baseinp, powinp))
