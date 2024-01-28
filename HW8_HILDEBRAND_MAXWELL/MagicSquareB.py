#This function makes a magic square
#Max Hildebrand
#4/18/23


def squareMaker(n):
    mSquare = [[0 for col in range(n)] for row in range(n)]
    mod = 2
    for count in range(len(mSquare)):
        mod -=1
        for x in range(len(mSquare[count])):
            mSquare[count][x] = (x+ mod)%n
    return mSquare
    printHelper(mSquare, 7)

def printHelper(Magic_Square, size):
    for row in range(0, size):
        print('\n')
        for col in range(0, size):
            print('\t', Magic_Square[row][col], end = '')

#main
print()
print('This program makes a magic square.')
print()
size = int(input('what is the length of your square? '))
print(squareMaker(size))
printHelper(squareMaker(size), size)
