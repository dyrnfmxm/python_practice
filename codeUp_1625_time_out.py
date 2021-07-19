n = int(input())
arr = []

for i in range(n):
    arr.append(input())

for i in range(len(arr)):
    
    #print(arr[i])
    while True:
        sum = 0
        for j in arr[i]:
            sum += int(j)
            arr[i] = str(sum)
            #print(sum)
            #print(arr[i])
        if sum < 10:
            print(sum)
            break
        



    """
    for j in arr[i]:
        sum += int(j)

    while sum >= 10:
        for i in str(sum):
            temp += int(i)
        
"""
