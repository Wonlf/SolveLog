def rol(x, n):
    shiftBit = x << n
    shiftBit &= 255
    carryBit = x >> 8 - n
    return shiftBit | carryBit



def ror(x, n):
    shiftBit = x >> n
    carryBit = x << (8 - n)
    carryBit &= 255
    return shiftBit | carryBit
a = 192

a = rol(a, 3)
print(format(a, 'b'))


a = ror(a, 3)
print(format(a, 'b'))


