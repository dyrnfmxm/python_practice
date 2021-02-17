def star(n):
    if n == 0:
        return n
    print("*"*n)
    return star(n-1)

n = int(input())
star(n)
