n = int(input())
a = list(map(int,input().split()))
u = d = 0
for i in range(n-1):
    if a[i] < a[i+1]:
        u += 1
    elif a[i] > a[i+1]:
        d += 1
print(u,d)
