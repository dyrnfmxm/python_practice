import statistics

a, b = map(int,input().split())

arr = []

arr.append(a+b)
arr.append(a-b)
arr.append(a*b)

print(statistics.median(arr))
