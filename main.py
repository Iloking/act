def findBit(number, n):
    if number & (1 << (n-1)):
        print(f"{n}th is a SET (1) bit")
    else:
        print(f"{n}th is not a SET (0) bit")


number = int(input("Enter the number: "))
print("Binary representation:", bin(number))
n = int(input("Position of the bit from the right side: "))
findBit(number, n)
