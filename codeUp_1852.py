def num(n,i):
    if i == n:
        return i
    print(i,end=' ')
    i += 1
    return num(n,i)
n = int(input())
i = 1
print(num(n,i))
