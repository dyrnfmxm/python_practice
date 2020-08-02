a, b, c = map(int,input().split())
if a >= b and a >= c:
    ma = a
    if b >= c:
        mid = b
        mi = c
    elif b <= c:
        mid = c
        mi = b
elif b >= a and b >= c:
    ma = b
    if a >= c:
        mid = a
        mi = c
    elif a <= c:
        mid = c
        mi = a
elif c >= b and c >= a:
    ma = c
    if b >= a:
        mid = b
        mi = a
    elif b <= a:
        mid = a
        mi = b

print('%d %d %d'%(mi,mid,ma))
