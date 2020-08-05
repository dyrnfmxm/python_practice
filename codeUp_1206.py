a,b = map(int,input().split())

if a%b == 0:
    x = int(a/b)
    print('%d*%d=%d'%(b,x,a))
elif b%a == 0:
    x = int(b/a)
    print('%d*%d=%d'%(a,x,b))
else:
    print("none")
