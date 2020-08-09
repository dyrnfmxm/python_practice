a,b = map(float,input().split())
#print(a,b)
while True:
    print('%.2f'%a,end=" ")
    a = round(a + 0.01,2)
    if a == b:
        print('%.2f'%a)
        break
