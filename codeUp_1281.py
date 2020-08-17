a, b = map(int,input().split())
if a%2 == 0:
    s = -a
    print('-%d'%a,end='')
elif a%2 == 1:
    s = a
    print(a,end='')
for i in range(a+1,b+1):
    if i%2 == 0:
        s = s-i
        print('-%d'%i,end='')
    elif i%2 == 1:
        s = s+i
        print('+%d'%i,end='')
print('=%d'%s)

