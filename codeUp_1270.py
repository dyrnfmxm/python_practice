n = int(input())
count = 0
for i in range(n+1):
    if i  % 10 == 1:
        count += 1
print(count)
