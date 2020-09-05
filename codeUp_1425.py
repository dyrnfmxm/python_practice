n, c = map(int,input().split())
h = list(map(int,input().split()))
h.sort()
count = tc = 0
while True:
    if count == c:
        print()
        count = 0
    elif tc == n:
        break
    else:
        print(h[0],end=' ')
        del h[0]
        count += 1
        tc += 1
