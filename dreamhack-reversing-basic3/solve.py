values = [73, 96, 103, 116, 99, 103, 66, 102, 128, 120, 105, 105,
          123, 153, 109, 136, 104, 148, 159, 141, 77, 165, 157, 69]

index = 33

result = ''


for i in range(0, len(values)):
    for index2 in range(33, 122):
        if((values[i]) == (i ^ index2) + 2 * i):
            result += chr(index2)

print(result)