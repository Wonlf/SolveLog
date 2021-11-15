values = [172, 243, 12, 37, 163, 16, 183, 37, 22, 198, 183, 188,
7, 37, 2, 213, 198, 17, 7, 197, 12]


result = ''


for i in range(len(values) - 1):
    for j in range(33, 125):
       if((j * -5) & 0xFF == values[i]):
            result += chr(j)

print(result)