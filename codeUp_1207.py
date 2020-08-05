a = list(map(int,input().split()))
count = 0
for i in range(len(a)):
    if a[i] == 1:
        count += 1
if count == 0:
    print("모")
elif count == 1:
    print("도")
elif count == 2:
    print("개")
elif count == 3:
    print("걸")
elif count == 4:
    print("윷")
