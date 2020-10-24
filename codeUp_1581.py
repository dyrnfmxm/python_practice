def myswap(a, b):
    if a > b:
        t = a
        a = b
        b = t
    print(a, b)

a, b = map(int,input().split())
myswap(a,b)
