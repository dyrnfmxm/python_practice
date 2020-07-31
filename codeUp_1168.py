a, b = map(int,input().split())
y = int(a/10000)
if b == 1 or b == 2:
    print(112-y+1)
else:
    print(12-y+1)
