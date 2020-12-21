def sum(n,s):
    if n < 1:
        return s
    s += n
    return sum(n-1,s)

n = int(input())
s = 0
print(sum(n,s))
