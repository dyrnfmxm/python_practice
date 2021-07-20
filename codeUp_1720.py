"""
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))


for i in arr:
    if min(i[0:3]) != i[3]:
        print(i)
"""

n = int(input())
error = 0

for i in range(n):
    arr = list(map(int,input().split()))
    if min(arr[:3]) != arr[-1]:
        print(i+1, min(arr[:3]))
        error += 1
    continue

if error == 0:
    print(-1)
