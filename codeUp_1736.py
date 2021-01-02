second = int(input())
d = h = m = s = 0
s = second%60
m = int(second/60)
h = int(m/60)
d = int(h/24)

m = m % 60
h = h % 24

print(d, h, m, s)

