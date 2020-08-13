k, h = map(int,input().split())
n = 0
if k % 2 == 1:
    for i in range(0,k,2):
        n += 1
elif k % 2 == 0:
    for i in range(0,k,2):
        n += 10
if h % 2 == 1:
    for i in range(0,h,2):
        n += 1
elif h % 2 == 0:
    for i in range(0,h,2):
        n += 10
print(n)
