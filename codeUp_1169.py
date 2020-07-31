n = int(input())
y = 2012 - n + 1
#print(y)
y2 = y%100
#print(y2)
if y < 2000:
    print(y2, "1")
else:
    print(y2, "3")
