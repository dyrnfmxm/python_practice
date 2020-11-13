import sys
sys.setrecursionlimit(12345)

def f(n,s):
    if n > 0:
        s += n
        return f(n-1,s)
    elif n == 0:
        return s

n = int(input())
s = 0
print(f(n,s))
