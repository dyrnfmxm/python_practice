def lcm(n, m):
    if n > m:
        i = n
    elif m > n:
        i = m
    else:
        i = n
        
    while True:
        if i % n == 0 and i % m == 0:
            return i
        else:
            i += 1

n, m = map(int,input().split())
print(lcm(n, m))
