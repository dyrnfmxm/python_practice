n = int(input())
a = list(map(int,input().split()))

for i in range(n):
    print(a[i],end=' ')
    if i < n-1:
        a[i+1] += a[i]
