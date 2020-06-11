n = int(input())
arr = list(map(float,input().split()))
#print(arr)
m = max(arr)
avg = 0
for i in range(n):
    #if arr[i] < m:
    arr[i] = arr[i]/m*100
    avg += arr[i]
#print(arr)
print(avg/n)
    
