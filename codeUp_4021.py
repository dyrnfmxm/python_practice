a = list(map(int,input().split()))
s = 0
for i in a:
    if i % 2 == 1:
        s += i
if s == 0:
    print(-1)
else:
    print(s)
