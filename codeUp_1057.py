a, b = map(int,input().split())
c = not a and not b
d = a and b
print(int(c or d))
