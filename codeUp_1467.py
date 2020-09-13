n,m = map(int,input().split())
for i in range(n,0,-1):
    c = n*m-i+1
    for j in range(m):
        print(c,end=' ')
        c -= n
    print()
