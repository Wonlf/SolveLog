values = [
    173, 216, 203, 203, 157, 151, 203, 196, 146, 161,
    210, 215, 210, 214, 168, 165, 220, 199, 173, 163, 
    161, 152, 76, 9
]

result = [0, ] * len(values) 

r_result = ''

values.reverse() 

for i in range(1, len(values)): 
    result[i] = values[i] - result[i-1] 
    
result.reverse() 

for i in range(len(result)): 
    r_result += chr(result[i])



print(r_result)
