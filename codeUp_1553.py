def cel(n):
    if n > 0:
        return int(n)+1
    elif n < 0:
        return int(n)
    elif n == 0:
        return 0
n = float(input())
print(cel(n))
