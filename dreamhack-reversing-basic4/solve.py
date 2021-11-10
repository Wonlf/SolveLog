values = [
    36, 39, 19, 198, 198, 19, 22, 230, 71, 245, 38, 150,
    71, 245, 70, 39, 19, 38,38 , 198, 86, 245, 195, 195, 
    245, 227, 227
]

result = ''


for i in range(0, len(values)):
    for j in range(33, 122):
        if (((16 * j) & 240 | (j >> 4)) == values[i]):
            result += chr(j)

print(result)