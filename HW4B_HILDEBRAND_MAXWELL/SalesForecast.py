#This program does a widget industry sales forecast
#Max Hildebrand
#3/2/2023


print("This program does a widget industry sales forecast")
while True:
    try:
        salesUW = int(input("Please enter initial sales for UW: "))
        salesWI = int(input("Please enter initial sales for WI: "))
        increaseUW = float(input("Please enter annual % increase for UW: "))/100
        increaseWI = float(input("Please enter annual % increase for WI: "))/100
        break
    except ValueError:
        print("incorrect value type! Try again.")


yearStart =int(input("Please enter the year to begin the forecast: "))
yearEnd =int(input("Please enter the year to end the forecast: "))
salesCross = 0
yearDiff = yearEnd - yearStart
decider = ''


if salesUW > salesWI:
    decider = "UW"
elif salesWI > salesUW:
    decider = "WI"


if yearDiff >= 10 and yearDiff <= 15:
    print()
    print("Year \t UW \t WI")
    print()
    for year in range(yearStart, yearEnd+1):
        print(year, "\t", salesUW, "\t", salesWI)
        salesUW = round(salesUW * (1+increaseUW), 1)
        salesWI = round(salesWI * (1+increaseWI), 1)

        if decider == "UW":
            if salesWI >= salesUW:
                salesCross = year+1
                decider = 'done'
        else:
            if salesUW >= salesWI:
                salesCross = year+1
                decider = 'done'
    if salesCross > 0:
        print("The sales crossed in ", salesCross)
    elif decider == '':
        print("The sales started out equal in ", yearStart)
    else:
        print("The sales never crossed.")
else:
    print("You asked for the wrong number of years (must be 10-15)")

    
    
