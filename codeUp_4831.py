n = int(input())
arr = list(map(int,input().split()))
c = 0

for i in arr:
    if i == n%10:
        c += 1
print(c)
