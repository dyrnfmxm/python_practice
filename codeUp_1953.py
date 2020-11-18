def star(n,c):
    if n == 0:
        return 0
    print("*"*c)
    c += 1
    return star(n-1,c)

n = int(input())
c = 1
star(n,c)
