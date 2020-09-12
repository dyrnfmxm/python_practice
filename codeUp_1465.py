n,m = map(int,input().split())
for i in range(n,0,-1):
    c = (i-1)*m+1
    for j in range(m):
        print(c,end=' ')
        c += 1
    print()
