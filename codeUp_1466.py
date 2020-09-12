n,m = map(int,input().split())
for i in range(n):
    c = n*m-i
    for j in range(m):
        print(c,end=' ')
        c -= n
    print()
