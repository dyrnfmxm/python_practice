a, b = map(int,input().split())
s = 0
for i in range(a,b+1):
    if i%2 == 0:
        s = s-i
    elif i%2 == 1:
        s = s+i
print(s)
