n = int(input())
a = []
for i in range(n):
    a.append(input())

for i in range(len(a)):
    print(a[i][::-1])
