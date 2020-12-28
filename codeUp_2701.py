n = int(input())
a = list(map(int,input().split()))
l = []
for i in a:
    l.append(abs(n-i))

print(min(l))
