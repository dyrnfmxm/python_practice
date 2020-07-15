n = int(input())
arr = []
for i in range(23):
    arr.append(0)
arr2 = list(map(int,input().split()))
for i in range(n):
    if arr2[i] == 1:
        arr[0] += 1
    elif arr2[i] == 2:
        arr[1] += 1
    elif arr2[i] == 3:
        arr[2] += 1
    elif arr2[i] == 4:
        arr[3] += 1
    elif arr2[i] == 5:
        arr[4] += 1
    elif arr2[i] == 6:
        arr[5] += 1
    elif arr2[i] == 7:
        arr[6] += 1
    elif arr2[i] == 8:
        arr[7] += 1
    elif arr2[i] == 9:
        arr[8] += 1
    elif arr2[i] == 10:
        arr[9] += 1
    elif arr2[i] == 11:
        arr[10] += 1
    elif arr2[i] == 12:
        arr[11] += 1
    elif arr2[i] == 13:
        arr[12] += 1
    elif arr2[i] == 14:
        arr[13] += 1
    elif arr2[i] == 15:
        arr[14] += 1
    elif arr2[i] == 16:
        arr[15] += 1
    elif arr2[i] == 17:
        arr[16] += 1
    elif arr2[i] == 18:
        arr[17] += 1
    elif arr2[i] == 19:
        arr[18] += 1
    elif arr2[i] == 20:
        arr[19] += 1
    elif arr2[i] == 21:
        arr[20] += 1
    elif arr2[i] == 22:
        arr[21] += 1
    elif arr2[i] == 23:
        arr[22] += 1
for i in range(23):
    print(arr[i],end=' ')
