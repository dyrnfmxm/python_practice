n = int(input())
es = gs = 100
for i in range(n):
    a, b = map(int,input().split())
    if a > b:
        gs -= a
    elif a < b:
        es -= b
print(es)
print(gs)
