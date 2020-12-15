def star(n):
    if n == 1:
        return '*'
    print('*',end='')
    return star(n-1)

n = int(input())
print(star(n))
