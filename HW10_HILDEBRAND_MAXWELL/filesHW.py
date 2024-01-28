#This program imports a text file about restaraunts and returns data about them
#Max Hildebrand
#5/1/2023


restFile = open('restaurants.txt','r')
linez = restFile.readlines()

rest2DList = [[s.lstrip().rstrip() for s in x.split(',')]for x in linez]
name, city, cuisine, cost, rating = 0, 1, 2, 3, 4

highResRate = 0
highRes = ''
lowResRate = 5
lowRes = ''
cuisines = []
cuisineRate = []
highest_cuisine_rating = 0
highest_cuisine = ''
lowest_cuisine_rating = 5
lowest_cuisine = ''
highest_expense = 0
expensive_restaurants = ''

for nest in range(len(rest2DList)):
    res_rating = float(rest2DList[nest][rating])
    if res_rating > highResRate:
        highResRate = res_rating
        highRes = rest2DList[nest][name]
        
    if res_rating < lowResRate:
        lowResRate = res_rating
        lowRes = rest2DList[nest][name]
        
    if rest2DList[nest][cuisine] not in cuisines:
        cuisines.append(rest2DList[nest][cuisine])
        cuisineRate.append([rest2DList[nest][cuisine]])
        
    for i in range(len(cuisineRate)):
        if rest2DList[nest][cuisine] == cuisineRate[i][0]:
            cuisineRate[i].append(rest2DList[nest][rating])
            
    if len(rest2DList[nest][cost]) >= highest_expense:
        if len(rest2DList[nest][cost]) == highest_expense:
            expensive_restaurants = expensive_restaurants + ", " + rest2DList[nest][name]
        else:
            highest_expense = len(rest2DList[nest][cost])
            expensive_restaurants = rest2DList[nest][name]


for x in range(len(cuisineRate)):
    avgRating = 0
    for y in range(1,len(cuisineRate[x])):
        avgRating = (avgRating + float(cuisineRate[x][y]))/y
        
    if avgRating > highest_cuisine_rating:
        highest_cuisine_rating = avgRating
        highest_cuisine = cuisineRate[x][0]
        
    if avgRating < lowest_cuisine_rating:
        lowest_cuisine_rating = avgRating
        lowest_cuisine = cuisineRate[x][0]
        
print("This program opens a text file and returns data about restaraunts.\n")
print(highRes,"is the restaurant with the highest rating, with a score of",highResRate)
print()
print(lowRes,"is the restaurant with the lowest rating, with a score of",lowResRate)
print()
print(expensive_restaurants,"are the most expensive restaurants, with a score of","$"*highest_expense)
print()
print("The different cuisines are:",cuisines)
print()
print(highest_cuisine,"is the cuisine with the highest average rating, with a score of",highest_cuisine_rating)
print()
print(lowest_cuisine,"is the cuisine with the lowest average rating, with a score of",lowest_cuisine_rating)
