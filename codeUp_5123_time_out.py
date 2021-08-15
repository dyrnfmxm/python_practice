n = int(input())

arr = list(map(int,input().split()))
count = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i]+arr[j])%3 == 0:
            count += 1
        #print(arr[i], arr[j])

print(count)
