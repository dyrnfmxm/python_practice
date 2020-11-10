def f(i,n):
    if i <= n:
        print(i)
        return f(i+1,n)
    
n = int(input())
i = 1
f(i,n)
