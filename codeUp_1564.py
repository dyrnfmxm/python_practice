def gcd(a,b):
    arr1 = []
    arr2 = []
    gcd = []
    for i in range(1,a+1):
        if a % i == 0:
            arr1.append(i)
    for j in range(1,b+1):
        if b % j == 0:
            arr2.append(j)

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                gcd.append(arr2[j])
    return max(gcd)


a, b = map(int,input().split())
print(gcd(a,b))
