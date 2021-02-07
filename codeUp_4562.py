a = int(input())
b = int(input())
c = int(input())

result = a * b * c
print(result)

#result = str(result)

arr = [0]*10

for i in result:
    i = int(i)
    arr[i] += 1

for i in arr:
    print(i)
