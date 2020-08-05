menu = 400, 340, 170, 100, 70
#print(menu)
a, b = map(int,input().split())
s = menu[a-1]+menu[b-1]
#print(s)
if s > 500:
    print("angry")
else:
    print("no angry")
