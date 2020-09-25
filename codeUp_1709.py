n = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)
for i in range(n):
    print(a[i],end=' ')
