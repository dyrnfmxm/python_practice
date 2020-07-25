y, m, d = map(int,input().split())
result = y-m+d
if result%10 == 0:
    print("대박")
else:
    print("그럭저럭")
