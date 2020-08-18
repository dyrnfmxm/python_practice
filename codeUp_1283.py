a = int(input())
b = int(input())
c = a
bList = list(map(int,input().split()))
for i in range(len(bList)):
    c = c + (c * bList[i]/100)
result = c - a
print(int(round(result,0)))

if result == 0:
    print("same")
elif result < 0:
    print("bad")
else:
    print("good")
