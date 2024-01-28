#This program converts Celcius temperatures to farenheit and farenheit tempuratures to celcius

def ftoc(tmp):
    tempC = round((tmp-32) * (.555), 1)
    return tempC

def ctof(tmp):
    tempF = round((1.8)*temp + 32, 1)
    return tempF


print("This program converts Celcius temperatures to fahrenheit and fahrenheit tempuratures to celcius")

temp = int(input("Enter the temperature: "))
scale = input("Which scale? F for Fahrenheit or C for Celcius: ")

scale = scale.upper()
scale = scale[0]

if scale == "F":
    answer = ftoc(temp)
    print(temp, "degrees Fahrenheit is",answer,"degrees Celcius")
else:
    answer = ctof(temp)
    print(temp, "degrees Celcius is",answer,"degrees Fahrenheit")
