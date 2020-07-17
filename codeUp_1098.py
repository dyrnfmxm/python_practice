h, w = map(int,input().split())
arr = [[0 for col in range(w)] for row in range(h)]
n = int(input())
for i in range(n):
    l, d, x, y = map(int,input().split())
    arr[x-1][y-1] = 1
    if d == 0:
        for j in range(y, y+l-1):
            arr[x-1][j] = 1
    elif d == 1:
        for k in range(x, x+l-1):
            arr[k][y-1] = 1
for i in range(h):
    for j in range(w):
        print(arr[i][j],end=' ')
    print()
