n = int(input())
a = 10
count = 1
while int(n/a) != 0:
    a *= 10
    count += 1
print(count)
