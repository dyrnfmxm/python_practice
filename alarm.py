h, m = input().split()
h = int(h)
m = int(m)

if m <45:
    h = h-1
    if h == -1:
        h = 23
    m = 60 - abs(m-45)
    print(h, m)
else:
    m = m - 45
    print(h, m)
