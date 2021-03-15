n = input()
count = 0

while n != n[::-1]:
    nn = int(n) + int(n[::-1])
    n = str(nn)
    count += 1

print(count, n)
