def fac(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * fac(a-1)
n, r = map(int,input().split())

nu = fac(n)
de = fac(n-r)*fac(r)
result = int(nu/de)
print(result)
