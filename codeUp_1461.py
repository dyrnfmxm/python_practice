n = int(input())
for i in range(n):
    c = (i+1)*n
    for j in range(n):
        print(c,end=' ')
        c -= 1
    print()
