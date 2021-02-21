arr = [0]*101
s = 0
for i in range(10):
    n = int(input())
    s += n
    arr[int(n/10)] += 1
print(int(s/10))
print(arr.index(max(arr))*10)
