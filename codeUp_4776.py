a = [i for i in range(10)]

b = 'ABCDEFGHIJKL'

n = int(input())

n = n-4

n = n%60

#print(n)

arr = []

for i in range(60):
    arr.append(b[i%12]+str(a[i%10]))

print(arr[n])
