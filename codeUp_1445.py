a_len, b_len = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
arr = a+b
arr.sort()

for i in arr:
    print(i,end=' ')
