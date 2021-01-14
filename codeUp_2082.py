n, k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    if k == a[i]:
        print(i+1)
        break
    elif i == n-1:
        print(-1)
    
