n, m = map(int,input().split())
arr = list(map(int,input().split()))

sum_arr = []
s = 0
for i in arr:
    s += i
    sum_arr.append(s)
#print(sum_arr)

for i in range(m):
    a, b = map(int,input().split())
    if a == 1:
        print(sum_arr[b-1])
    else:
        print(sum_arr[b-1] - sum_arr[a-2])
    
