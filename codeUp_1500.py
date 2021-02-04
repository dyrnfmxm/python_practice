n, m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(n):
    for j in a[i]:
        print(j,end=' ')
    print()
