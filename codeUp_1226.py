lotto = list(map(int,input().split()))
a = list(map(int,input().split()))
count = 0
b = 0
for i in range(len(lotto)-1):
    for j in range(len(a)):
        if lotto[i] == a[j]:
            count += 1
if count == 6:
    print("1")
elif count == 5:
    for i in range(len(a)):
        if lotto[6] == a[i]:
            b = 1
    if b == 1:
        print("2")
    else:
        print("3")
elif count == 4:
    print("4")
elif count == 3:
    print("5")
else:
    print("0")
        
