n, m = map(int,input().split())
a = [[0] * m for _ in range(n)]
i = n-1
j = m-1
c = 1
while True:
    if n % 2 == 1:
        if i % 2 == 0:                    
            a[i][j] = c
            c += 1
            j -= 1
            if j < 0:
                i -= 1
                j += 1
        elif i % 2 == 1:
            a[i][j] = c
            c += 1
            j += 1
            if j == m:
                i -= 1
                j -= 1
    elif n % 2 == 0:
        if i % 2 == 1:                    
            a[i][j] = c
            c += 1
            j -= 1
            if j < 0:
                i -= 1
                j += 1
        elif i % 2 == 0:
            a[i][j] = c
            c += 1
            j += 1
            if j == m:
                i -= 1
                j -= 1
    if i < 0:
        break
        
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()
