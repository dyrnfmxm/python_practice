n, m = map(int,input().split())
for i in range(m):
    if i == 0 or i == m-1:
        for j in range(n):
            if j == 0 or j == n-1:
                print("+",end='')
            else:
                print("-",end='')
    else:
        for j in range(n):
            if j == 0 or j == n-1:
                print("|",end='')
            else:
                print(" ",end='')
    print()
