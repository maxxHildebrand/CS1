#Max Hildebrand
#This program takes in a sample of widget scores and returns the median and mode.
#4/5/2023

import random

def mode(scoresList):
    modeNum = 0
    returnList = []
    modeList = [0 for x in range(10)]
    for count in range(len(scoresList)):
        modeList[int(scoresList[count])] += 1
    for counter in range(len(modeList)):
        if modeList[counter] >= modeNum:
            modeNum = modeList[counter]
    for step in range(len(modeList)):
        if modeList[step] == modeNum:
            returnList.append(step)
    
    return returnList

def median(medList):
    list2 = sortem(medList)
    median = (list2[len(list2) // 2])
    return median
    
    
    

def sortem(list1):
    for x in range(0, len(list1) - 1):
        minVal = list1[x]
        minIndex = x
        for idx in range(x + 1, len(list1)):
            if list1[idx] <= minVal:
                minVal = list1[idx]
                minIndex = idx
        list1[minIndex] = list1[x]
        list1[x] = minVal

    return list1

print('This program takes in a sample of widget scores and returns the median and mode.')
print()
numWidgets = str(random.randint(20, 30))
scores = input('Input ' + numWidgets + ' widget scores seperated by commas: ')
inputList = (scores.split(','))
print()
print('The median is:', median(inputList))
print('The mode(s) are:', mode(inputList))
