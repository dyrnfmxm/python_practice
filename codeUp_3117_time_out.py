n = int(input())

arr = []

for i in range(n):
    m = int(input())
    if m == 0:
        arr = arr[:-1]
        
    else:
        arr.append(m)

print(sum(arr))
