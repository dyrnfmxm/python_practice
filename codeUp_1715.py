from math import gcd

n, m = map(int,input().split())

gcd_num = gcd(n,m)

n = n//gcd_num
#print(n)

m = m//gcd_num
#print(m)

print(n, m)
