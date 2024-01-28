#This program creates an odd-sided Magic Square, where the sum of each row, column and diagonal adds up to the same number
#Max Hildebrand
#4/18/2023

import random


def squareMaker(n):
    Magic_Square = [[0 for col in range(n)] for row in range(n)]
    
    incount = 0
    rowOut = 0
    colOut = 0
    blocked = 0
    bothOut = 0
    
    row = 0
    col = n//2
    Magic_Square[row][col] = 1
    for count in range(2, n**2+1):
        row -=1
        col +=1
        if n-1 >= row and row >= 0 and n-1 >= col and col >= 0:
            if Magic_Square[row][col] == 0:
                
                Magic_Square[row][col] = count
                incount += 1
            else:
                row +=2
                col-=1
                Magic_Square[row][col] = count
                blocked += 1
        elif row < 0 and n-1 >= col >= 0:
            row = n-1
            Magic_Square[row][col] = count
            rowOut +=1
        elif col > n - 1 and n-1 >= row >=0:
            col = 0
            Magic_Square[row][col] = count
            colOut += 1
        else:
            row +=2
            col -= 1
            Magic_Square[row][col] = count
            bothOut += 1
    printHelper(Magic_Square, n)
    sum1 = sum(Magic_Square[1])
    print('\nThe sum of each row, column, and diagonal is:', sum1)
    return [incount, rowOut, colOut, blocked, bothOut, Magic_Square]
            
                
            
            


def recursiveFlatten(SQ):
    if SQ == []:
        return SQ
    else:
        return SQ[0] + recursiveFlatten(SQ[1:])


def printHelper(Magic_Square, size):
    for row in range(0, size):
        print('\n')
        for col in range(0, size):
            print('\t', Magic_Square[row][col], end = '')

def randomMatch(Magic_Square, size):
    flatList = recursiveFlatten(Magic_Square)
    print(flatList, 'Flattened 3x3\n')
    count = 0
    match = False
    while match == False:
        testList = []
        for x in range(size **2):
            same = False
            while same == False:
                num = random.randint(1,9)
                if num not in testList:
                    testList.append(num)
                    same = True
                    break
        count += 1
        if count % 100000 == 0:
            print(testList, 'at', count, 'attempts')
        if testList == flatList:
            match == True
            break
    print(flatList, '\n')
    print(testList, 'match')
    print('It took', count, 'tries to create a random square to match the original.')


#main
print('This program creates an odd-sided Magic Square,\n where the sum of each row, column, and diagonal\n adds up to the same number.')
print()
print('This program will also recordand print the various counts associated\n with specific moves during the construction of the square.')
print()
print('Lastly, and only for the 3x3 Magic Square,\n the program must count how many iterations it will take\n to randomly suplicate a Square that is a\n perfect duplicate of the 3x3 Magic Square.')

print()
size = int(input("Enter desired size of Magic_Square "))
Magic_Square = squareMaker(size)
print()
print('incount:', Magic_Square[0])
print('row out:', Magic_Square[1])
print('col out:', Magic_Square[2])
print('blocked:', Magic_Square[3])
print('both out:', Magic_Square[4])
print()
if size == 3:
    randomMatch(Magic_Square[5],size)


print('Program End')
