a, b, c = map(int,input().split())
gcd = []
for i in range(1,a+1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        gcd.append(i)
print(max(gcd))
