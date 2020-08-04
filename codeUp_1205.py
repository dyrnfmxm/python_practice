a, b = map(float,input().split())

n1 = a+b

if a-b > b-a:
    n2 = a-b
else:
    n2 = b-a

n3 = a*b

if a/b > b/a:
    n4 = a/b
else:
    n4 = b/a

if a**b > b**a:
    n5 = a**b
else:
    n5 = b**a

print('%.6f'%(max(n1,n2,n3,n4,n5)))
