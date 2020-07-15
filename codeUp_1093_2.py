n = int(input())
b = input().split()

#print(b)
arr = []
for i in range(23):
    arr.append(0)
#print(arr)

for i in range(n):
    arr[int(b[i])-1] += 1

#print(arr)
for i in range(23):
    print(arr[i], end=' ')
