def rol(x, n):
    shiftBit = x << n
    shiftBit &= 255
    carryBit = x >> 8 - n
    return shiftBit | carryBit


a = [82, 223, 179, 96, 241, 139, 28, 181, 87, 209, 159, 56,
75, 41, 217, 38, 127, 201, 163, 233, 83, 24, 79, 184,
106, 203, 135, 88, 91, 57, 30, 0]

b = 33

result = ""

for index in range(len(a)):
    for index2 in range(b, 122):
        if(index ^ rol(index2 , (index & 7)) == a[index]):
            result = result + chr(index2)

print(result.split('>')[0])

