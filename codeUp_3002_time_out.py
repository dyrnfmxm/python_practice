n = int(input())

arr = list(map(int,input().split()))

m = int(input())

arr_2 = list(map(int,input().split()))

 

for i in arr_2:

    if i not in arr:

        print('-1', end=' ')

    else:

        for j in range(len(arr)):

            if i == arr[j]:

                print(j+1, end=' ')
