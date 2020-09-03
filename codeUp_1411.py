n = int(input())
a = list()
c = [0]*n
for i in range(n-1):
    a.append(int(input()))
    for j in range(1,n+1):
        if a[i] == j:
            c[j-1] += 1
for i in range(n):
    if c[i] == 0:
        print(i+1)
