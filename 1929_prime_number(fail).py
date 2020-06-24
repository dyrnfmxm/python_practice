a, b = map(int,input().split())
for i in range(a,b):
    c = True
    for j in range(2, i):
        if i%j == 0:
            c = False
            break
    if c:
        print(i)
