#This program screens for couples seeking low cost mortgage loans
#Max Hildebrand
#2/13/2023

#rate function determines the final interest rate

def rate(score1, score2):
    avg = (score1 + score2)/2
    print()
    print("For the Loan Officer: ")
    intRate = float(input("Enter the interest Rate: "))
    if avg >= 800:
        adjRate = intRate - (3/8)
    elif avg >= 775:
        adjRate = intRate - (1/4)
    elif avg >= 750:
        adjRate = intRate - (1/8)
    else:
        adjRate = intRate
    return adjRate



#main program starts here

print("This program screens for couples seeking low cost mortgage loans")
print()

qual = ""
print("For the Loan Officer: ")
medPrice = int(input("Enter the median price of homes in this area during the past 12 months: "))
print()

print("\n For the applicants:")
age1 = int(input("Person One, Enter your age: "))
age2 = int(input("Person Two, Enter your age: "))

if ((age1 >= 25 and age1 <= 30) or (age2 >= 25 and age2 <= 30)) and \
   ((age1 >=23 and age1<=35) and (age2 >=23 and age2<=35)):
    yrsDating = int(input("Enter years in relationship: "))
    if yrsDating >= 1 and yrsDating <= 5:
        empInfo = input("Both gainfully employed for 48 weeks? Y or N: ")
        if empInfo == "Y" or empInfo == 'y':
            homePrice = int(input("Enter the price of home: "))
            if homePrice <= (medPrice - 5000):
                print("\n Enter your credit scores: ")
                cred1 = int(input("Enter person 1's credit score: "))
                cred2 = int(input("Enter person 2's credit score: "))
                if(cred1 >= 650 and cred2 >= 650):
                    qual = "yes"

if qual == "yes":
    print("\n Congratulations! You have qualified.")
    resultRate = rate(cred1, cred2)
    print("Your interest rate is: ", resultRate)
else:
    print("\n Sorry, you did not qualify.")
    
