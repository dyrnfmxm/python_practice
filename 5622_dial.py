t = input()
count = 0
for i in range(len(t)):
    if t[i] in 'ABC':
        count += 3
    elif t[i] in 'DEF':
        count += 4
    elif t[i] in 'GHI':
        count += 5
    elif t[i] in 'JKL':
        count += 6
    elif t[i] in 'MNO':
        count += 7
    elif t[i] in 'PQRS':
        count += 8
    elif t[i] in 'TUV':
        count += 9
    elif t[i] in 'WXYZ':
        count += 10
print(count)
