y, m, d = map(int,input().split())
a = y + m + d
b = int(a / 100)
#print(b)
if b % 2 == 0:
    print("대박")
else:
    print("그럭저럭")
