#This program recursively converts a decimal number into binary
#Max Hildebrand
#4/24/23

def rCTB(binary, dec, L):
    if len(L) == 0:
        return binary
    else:
        if dec - L[0] >= 0:
            dec = dec - L[0]
            binary = binary + "1"
        else:
            binary = binary + "0"
        return rCTB(binary, dec, L[1:])

#main
binL = [2**7, 2**6, 2**5, 2**4, 2**3, 2**2, 2**1, 2**0]
binary = ""
print("This program recursively converts a decimal number into binary")
print()
num = int(input("Enter a number that you want to convert from dec to bin: "))
print(num,"in binary is",rCTB(binary, num, binL))
