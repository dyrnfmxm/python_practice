a, b, c = map(int,input().split())

if a >= b and a >= c:
    if a < b+c:
        print("yes")
    else:
        print("no")
elif b >= a and b >= c:
    if b < a+c:
        print("yes")
    else:
        print("no")
elif c >= b and c >= a:
    if c < b+a:
        print("yes")
    else:
        print("no")
