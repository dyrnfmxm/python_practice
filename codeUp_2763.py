a, b = map(int,input().split())
arr = []
for i in range(1,a+1):
    if a % i == 0 and  b % i == 0:
        arr.append(i)

if len(arr) == 1:
    print("coprime")
else:
    print("no")
