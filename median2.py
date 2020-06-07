a, b, c = map(int,input().split())
max_ = max(a, b, c)
min_ = min(a, b, c)
print(a + b + c - max_ - min_)
