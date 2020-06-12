n = int(input())
avg = 0
for i in range(n):
    sum = count = 0
    arr = list(map(int,input().split()))
    for j in range(1,(arr[0]+1)):
        sum += arr[j]
    avg = sum/arr[0]
    #print(avg)
    for k in range(1,arr[0]+1):
        if arr[k] > avg:
            count += 1
    #print(count)
    print('%0.3f'%((count/arr[0])*100)+"%")
