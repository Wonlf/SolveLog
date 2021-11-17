values = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43,
254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71,
240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253,
147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216,
49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128,
226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90,
160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0,
237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88,
207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2,
127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56,
245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12,
19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93,
25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238,
184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36,
92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200,
55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101,
122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232,
221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102,
72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158,
225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135,
233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230,
66, 104, 65, 153, 45, 15, 176, 84, 187, 22]

v5 = [74, 95, 97, 109, 95, 75, 69, 89]


# a1 = [0, ] * len(values) 




main = [
    0x7E, 0x7D, 0x9A, 0x8B, 0x25, 0x2D, 0x0D5, 0x3D, 3, 0x2B,
    0x38, 0x98, 0x27, 0x9F, 0x4F, 0x0BC, 0x2A, 0x79, 0,
    0x7D, 0x0C4, 0x2A, 0x4F, 0x58, 0, 0, 0, 0, 0, 0, 0, 0
]


# print(len(val))

def ror(x, n):
    shiftBit = x >> n
    carryBit = x << (8 - n)
    carryBit &= 255
    return shiftBit | carryBit


def rol(x, n):
    shiftBit = x << n
    shiftBit &= 255
    carryBit = x >> 8 - n
    return shiftBit | carryBit

#for i in range(0, 25):
    
    
# for index in range(33, 125):
#     if(val[0] == ror(index + values[v5[7] ^ index], 5)):
#         print(index)

result = ''

#main[1] = ror(a[1] + values[v5[0] ^ a[0]], 5) 
# for index in range(33, 122):
#     if(main[2] == rol(index + values[v5[1] ^ main[1]], 5)):
#         print(index)

# a = 5

# print(a)

# a = ror(a, 5)

# print(a)

# a = rol(a, 5)

# print(a)s

#print(values[v5[7] ^ main[7]]) 67


#0x7E = ror(n + 67, 5)

#print(rol(0x7E, 5) - values[v5[7] ^ main[7]])

#print(ror(140 + 67, 5))



# print(rol(main[2], 5) - values[v5[1] ^ main[1]])
# print(rol(main[3], 5) - values[v5[2] ^ main[2]])
# print(rol(main[4], 5) - values[v5[3] ^ main[3]])
# print(rol(main[5], 5) - values[v5[4] ^ main[4]])
# print(rol(main[6], 5) - values[v5[5] ^ main[5]])
# print(rol(main[7], 5) - values[v5[6] ^ main[6]])
# print(rol(main[0], 5) - values[v5[7] ^ main[7]])


# rol(0x7E, 5) == a[0] + values[v5[7] ^ 0]
# 207 ==  a[0] + values[v5[7] ^ 0]

#print(207 - values[v5[7] ^ 0])

#for i in range(7, 0,  -1):
    #print(i)
    #print(rol(main[i + 1], 5) - values[v5[i] ^ main[i]])

#print(rol(main[0], 5) - values[v5[7] ^ main[7]])


# for j in range(0, 8):
#     main[0] = ror(a[0] + values[v5[7] ^ main[7]], 5)

#     main[1] = ror(a[1] + values[v5[0] ^ main[0]], 5)
#     main[2] = ror(a[2] + values[v5[1] ^ main[1]], 5)
#     main[3] = ror(a[3] + values[v5[2] ^ main[2]], 5)
#     main[4] = ror(a[4] + values[v5[3] ^ main[3]], 5)
#     main[5] = ror(a[5] + values[v5[4] ^ main[4]], 5)
#     main[6] = ror(a[6] + values[v5[5] ^ main[5]], 5)
#     main[7] = ror(a[7] + values[v5[6] ^ main[6]], 5)

#    



# for i in range(0, 16):
#     for j in range(0,8):
#         for index in range(33, 125):
#             for asd in range(0, len(val)):
#                 if(ror(a1[(j + 1) & 7] + values[v5[j] ^ index], 5) == val[asd]):

#             # index = ror(a1[(j + 1) & 7] + values[v5[j] ^ index], 5)
#             # a1[(j + 1) & 7] = index
# print(a1)
# for j in range(0, 8):
#     for asd in range(0, len(val)):
#         for index in range(33, 125):
#             for index2 in range(33, 125):
#                 if(ror(index2 + values[v5[j] ^ index2], 5) == val[asd]):
#                     print(index2, index)
