"""n = int(input())
arr = [[0]*19]*29
for i in range(n):
    a, b = map(int,input().split())
    arr[int(a)-1][int(b)-1] += 1
    for i in range(19):
        for j in range(19):
            print(arr[i][j],end=' ')
        print()
"""
n = int(input())
arr = [[0 for col in range(19)] for row in range(19)]
for i in range(n):
    a, b = map(int,input().split())
    arr[int(a)-1][int(b)-1] = 1
for i in range(19):
    for j in range(19):
        print(arr[i][j],end=' ')
    print()
