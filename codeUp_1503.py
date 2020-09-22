n = int(input())
a = [[0] * n for _ in range(n)]
i = j = 0
c = 1

while True:
    if i % 2 == 0:
        a[i][j] = c
        c += 1
        j += 1
        if j == n:
            i += 1
            j -= 1
    elif i % 2 == 1:
        a[i][j] = c
        c += 1
        j -= 1
        if j < 0:
            i += 1
            j += 1
    if i == n:
        break
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
