 #This program calculates Maximum Heart Rate(MHR) and preferred Target Heart Rate(THR) Zones
#Max Hildebrand
#2/5/2023

def targetRate(objective, maxRate):
    if objective == 1:
        lower = round(maxRate * .6, 1)
        higher = round(maxRate * .69, 1)
        return str(lower) + " - " + str(higher)
    elif objective == 2:
        lower = round(maxRate * .7, 1)
        higher = round(maxRate * .79, 1)
        return str(lower) + " - " + str(higher)
    elif objective == 3:
        lower = round(maxRate * .8, 1)
        higher = round(maxRate * 1, 1)
        return str(lower) + " - " + str(higher)

print("This program calculates Maximum Heart Rate(MHR) and preferred Target Heart Rate(THR) Zones.")


age = int(input("How old are you? "))
MHR = 220-age
print("Your maximum heart rate is: ", MHR)

print("Please indicate your exercise objective as follows: ")
print("1 = weight loss, building endurance")
print("2 = weight management, improving cardio fitness")
print("3 = interval workouts")

obj = int(input("Enter your objective: "))

THR = targetRate(obj, MHR)

print("Your Target Heart Rate zone is: ", THR, " beats per minute.")
