def subsetsum(a,b):
    s = 0
    for i in range(a-1,b):
        s += ki[i]
    return s

n = int(input())
ki = list(map(int,input().split()))
a, b = map(int,input().split())
print(subsetsum(a,b))
