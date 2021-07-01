import math

def lcm(n, m):
    return n * m // math.gcd(n, m)

n, m = map(int,input().split())
print(lcm(n, m))
