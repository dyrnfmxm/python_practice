a = int(input())
b = input()
s = 0
for i in range(len(b)-1,-1,-1):
    if i == 2:
        s += a*int(b[i])
    elif i == 1:
        s += (a*int(b[i]))*10
    elif i == 0:
        s += (a*int(b[i]))*100
    print(a*int(b[i]))
print(s)
