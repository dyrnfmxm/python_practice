n = int(input())
a = [[0] * n for _ in range(n)]
i = j = 0
c = 1
while True:
    a[i][j] = c
    c += 1
    i += 1
    if i == n:
        j += 1
        i = 0
    if j == n:
        break
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
