n = int(input())
for i in range(1,7):
    if n-i <= 0 or n-i >= 7:
        continue
    print(i, n-i)
