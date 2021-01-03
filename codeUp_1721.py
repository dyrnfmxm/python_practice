x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())

x3 = x2-x1
y3 = y2-y1

l = x3**2 + y3**2

print('%.2f'%l**0.5)
