n = int(input())
s = i = 0
while True:
    s += i
    i += 1
    if s >= n:
        break
print(s)
