a, b, c = map(int,input().split())
r = a
if a >= b:
    r = b
if r >= c:
    r = r
print(int(r))
