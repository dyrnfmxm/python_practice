n,m = map(int,input().split())
c = n*m
for i in range(n):
    for j in range(m):
        print(c,end=' ')
        c -= 1
    print()
