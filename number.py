a = int(input())
b = int(input())
c = int(input())
m = a*b*c
#print(m)
arr = list(str(m))
#print(arr)
for i in range(10):
    print(arr.count(str(i)))
