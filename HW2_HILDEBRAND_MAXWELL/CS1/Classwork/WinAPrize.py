#This program awards a prize if conditions are met

print("\nThis program awards a prize if conditions are met")
print("Please answer in lower case")

food = input("\nWhat is your favorite kind of junk food? ")
temp = input("What is your favorite temperature? ")
music = input("What is your favorite kind of music? ")

if music == 'metal' and food == 'oreos' and temp == 'torrid':
    print('\nYou win 3 days in a sensory deprivation chamber!!')
else:
    print("\nYou do not win")
