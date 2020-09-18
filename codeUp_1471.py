n = int(input())
a = [[0] * n for _ in range(n)]
c = 1
i = n-1
j = 0
while True:
    if j % 2 == 0:
        a[i][j] = c
        c += 1
        i -= 1
        if i < 0:
            j += 1
            i += 1
    elif j % 2 == 1:
        a[i][j] = c
        c += 1
        i += 1
        if i == n:
            j += 1
            i -= 1
    if j == n:
        break
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
