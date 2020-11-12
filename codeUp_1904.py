def f(a, b):
    if a <= b:
        if a % 2 == 1:
            print(a,end=' ')
        return f(a+1,b)

a, b = map(int,input().split())
f(a,b)
