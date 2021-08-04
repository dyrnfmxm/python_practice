n = int(input())

a = list(map(int,input().split()))

num = 1

for i in a:
    num *= i

print(num % 2013)
