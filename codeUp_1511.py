n = int(input())
a = [[0] * n for _ in range(n)]
c = 1
s = 0
for i in range(n):
    if i == 0 or i == n-1:
        for j in range(n):
            a[i][j] = c
            c += 1
            s += a[i][j]
    else:
        for j in range(n):
            a[i][j] = c
            c += 1
            if j == 0 or j == n-1:
                s += a[i][j]

print(s)
