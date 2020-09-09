n= int(input())
for i in range(n):
    c = i+1
    for j in range(n):
        print(c,end=' ')
        c += n
    print()
