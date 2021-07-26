n = int(input())

arr = list(map(int,input().split()))

k = int(input())
c = 0

if k not in arr:
    print('-1')
else:
    for i in range(len(arr)):
        if arr[i] == k:
            print(i+1)
            break
