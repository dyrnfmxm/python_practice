def f(n,c):
    if n == 1:
        c += 1
        return c
    elif n % 2 == 0:
        c += 1
        return f(int(n/2),c)
    elif n % 2 == 1:
        c += 1
        return f((3*n+1),c)
n = int(input())
c = 0
print(f(n,c))
