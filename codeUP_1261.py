a = list(map(int,input().split()))
count = 0
for i in range(len(a)):
    if a[i] % 5 == 0:
        print(a[i])
        break
    else:
        count += 1
if count == len(a):
    print("0")
