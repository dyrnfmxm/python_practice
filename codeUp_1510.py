n = int(input())
a = [[0] * n for _ in range(n)]

c = i = 0
j = int(n/2)
while c <= (n*n)-1:
    c += 1
    a[i][j] = c
    if c % n == 0:
        i += 1
        if i == n:
            i = 0
    else:
        i -= 1
        if i < 0:
            i = n-1
        j += 1
        if j == n:
            j = 0

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
