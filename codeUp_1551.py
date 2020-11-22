def f(k):
    for i in range(len(a)):
        if k == a[i]:
            print(i+1)
            break
        elif i == len(a)-1:
            print(-1)

n = int(input())
a = list(map(int,input().split()))
k = int(input())
f(k)
