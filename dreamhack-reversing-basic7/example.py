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


print(format(rol(192, 3), 'b'))
print(format(192 << 3, 'b'))


