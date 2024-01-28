def rGcd(num1, num2):
    if num1%num2 == 0:
        return num2
    else:
        num2, num1 = num1, num1 % num2
        return rGcd(num2, num1)

print()
print('This program recursively finds the Greatest Common Denominator.')
print()
m = int(input('Enter the first number: '))
n = int(input('Enter the second number: '))
print('Recursive')
print(rGcd(m, n))
