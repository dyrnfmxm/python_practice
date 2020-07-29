a = list(map(int,input().split()))
b = 0
for i in range(len(a)):
    if a[i] <= 170:
        b = "CRASH"
        break
    else:
        b = "PASS"
print(b)
