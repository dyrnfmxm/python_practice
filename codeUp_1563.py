def mid(n, m, x):
    if n >= m:
        if m >= x:
            return m
        elif x >= m:
            if n >= x:
                return x
            else:
                return n
    elif m >= n:
        if n >= x:
            return n
        elif x >= n:
            if m >= x:
                return x
            else:
                return m
            
n, m, x = map(int,input().split())
print(mid(n,m,x))
