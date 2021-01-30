n = int(input())
count = 0

money = [50000,10000,5000,1000,500,100,50,10]

for i in money:
    count += int(n/i)
    n = int(n%i)

print(count)
