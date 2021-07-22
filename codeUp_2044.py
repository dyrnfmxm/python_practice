s = input()

result = []

for i in s:
    if i == '0' or i == '1' or i == '2':
        result.append(i)
    elif i == 'A':
        result = result[:-1]
    elif i == 'B':
        result = result[:-2]
    elif i == 'C':
        result = []

for i in result:
    print(i,end='')
