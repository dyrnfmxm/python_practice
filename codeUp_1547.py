def prime(n):
    c = 0
    for i in range(1,n):
        if n % i == 0:
            c += 1
    if c == 1:
        return "prime"
    else:
        return 'composite'

n = int(input())
print(prime(n))
