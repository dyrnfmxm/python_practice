def max(n,m):
    if n >= m:
        return n
    elif n < m:
        return m
n,m = map(int,input().split())
print(max(n,m))
