n = int(input())

num = 0
for i in range(n):
    num += i+1

for i in range(1,n+1):
    for j in range(i):
        print(num,end=' ')
        num -= 1
    print()
