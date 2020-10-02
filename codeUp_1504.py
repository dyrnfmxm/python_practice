n = int(input())
a = [[0] * n for _ in range(n)]
i = j = c = 0

while True:
    c += 1
    if j % 2 == 0:
        a [i][j] = c
        i += 1
        if i == n :
            i -= 1
            j += 1
    elif j % 2 == 1:
        a[i][j] = c
        i -= 1
        if i < 0:
            i += 1
            j += 1
    if j == n:
        break



for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
