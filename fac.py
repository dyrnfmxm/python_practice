n = int(input("어디까지 계산할까요"))
fac = 1
for i in range(1,n+1):
    fac *= i

print(n, "!는 ", fac)
