n= int(input())
for i in range(n,0,-1):
    c = i
    for j in range(n):
        print(c,end=' ')
        c += n
    print()
