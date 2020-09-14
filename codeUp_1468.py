n = int(input())
for i in range(n):
    if i % 2 == 0:
        c = i*n+1
        for j in range(n):
            print(c,end=' ')
            c += 1
    elif i % 2 == 1:
        c = (i+1)*n
        for j in range(n):
            print(c,end=' ')
            c -= 1
    print()
