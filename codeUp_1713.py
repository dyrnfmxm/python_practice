a, b = map(int,input().split())
s = 0
for i in range(a,b+1):
    if i%3 == 0 and i%4 == 0:
        continue
    elif i%3 == 0:
        s += i
    elif i%4 == 0:
        s -= i

print(s)
