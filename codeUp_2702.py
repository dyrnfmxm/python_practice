n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

#print(arr)

i = j = s = 0
a = []
while True:
#    print(arr[i][j])
    a. append(arr[i][j])
    i += 1
    if i == n:
        s += max(a)
        a = []
        i = 0
        j += 1
        if j == len(arr[i]):
            break
print(s)
