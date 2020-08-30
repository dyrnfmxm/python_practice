n = int(input())
a = list(map(int,input().split()))

for i in range(n):
    for j in range(i, n+i):
        if j >= n:
            j = abs(n-j)
        print(a[j],end=' ')
    print()
