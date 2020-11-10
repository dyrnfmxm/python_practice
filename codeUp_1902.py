def f(n):
    if n > 0:
        print(n)
        return f(n-1)

n = int(input())
f(n)
