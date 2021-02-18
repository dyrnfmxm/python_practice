def star(n,i):
    if i > n:
        return i
    print("*"*i)
    return star(n,i+1)

n = int(input())
star(n,1)
