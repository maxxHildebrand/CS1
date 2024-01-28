import random


def encode(msg):
    offset = random.randint(1,25)
    newMsg = ''
    for x in msg:
        newMsg += chr(ord(x) + offset)
        for count in range(random.randint(1,3)):
            newMsg += chr(random.randint(33, 64))
    return newMsg

def strip(codedMsg):
    noSpaceMsg = ''
    for let in codedMsg:
        if let != ' ':
            noSpaceMsg += let
    
    strippedMsg = ''
    for letter in noSpaceMsg:
        if ord(letter) > 64:
            strippedMsg += letter
    return strippedMsg

def decode(reducedEncoded):
    counter = 0
    while counter < 25:
        newMsg = ''
        for letter in reducedEncoded:
            newMsg += chr(ord(letter) - counter)
        if 'crypt' in newMsg:
            return newMsg
        else:
            counter+=1

            

#main

print("This program encodes a message and then reduces and decodes the message.")

print("Please enter a message you would like encoded with the embedded key code")
message = input("Enter message here: ")

encoded = encode(message)
encoded = encoded.lower()
print("lower case string is: ")
print(encoded)
print()
reducedEncoded = strip(encoded)
print("With the specials stripped out the string is: ")
print(reducedEncoded)
print()
decoded = decode(reducedEncoded)
print()
print('The decoded string is: ')
print(decoded)

#end program

