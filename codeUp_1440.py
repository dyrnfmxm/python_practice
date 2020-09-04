n = int(input())
a = list(map(int,input().split()))

for i in range(n):
    print("%d:"%(i+1),end=' ')
    for j in range(n):
        if i == j:
            continue
        elif a[i] < a[j]:
            print("<",end=' ')
        elif a[i] > a[j]:
            print(">",end=' ')
        else:
            print("=",end=' ')
    print()
