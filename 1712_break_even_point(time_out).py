a, b, c = map(int,input().split())
n = 1
while True:
    if b>=c:
        print(-1)
        break
    elif (a+(b*n)) < (c*n):
        print(n)
        break
    else:
        n += 1
