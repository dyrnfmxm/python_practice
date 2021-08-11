n = int(input())
result = 0
if n <= 500:
    result = n * 70/100
elif n > 500 and n <= 1500:
    result = 350 + (n - 500) * 40/100
elif n > 1500 and n <= 4500:
    result = 750 + (n - 1500) * 15/100
elif n > 4500 and n <= 10000:
    result = 1200 + (n - 4500) * 5/100
elif n > 10000:
    result = 1475 + (n - 10000) * 2/100

print(int(result))
