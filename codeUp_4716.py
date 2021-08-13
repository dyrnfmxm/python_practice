arr = []
p = 0

for i in range(10):
    a, b = map(int,input().split())

    p = p - a + b

    arr.append(p)


print(max(arr))
