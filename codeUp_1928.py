def f(n):
    print(int(n))
    if n == 1:
        return 1
    elif n % 2 == 1:
        return f(n*3+1)
    else:
        return f(n/2)

n = int(input())
f(n)
