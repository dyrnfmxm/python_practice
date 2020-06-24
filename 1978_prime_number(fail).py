n = int(input())
arr = list(map(int,input().split()))
count = 0
for i in arr:
    b = True
    for j in range(2,i):
        if i&j == 0:
            b = False
            break
    if b:
        count += 1
print(count)
