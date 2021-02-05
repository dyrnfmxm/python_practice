import statistics

a = []
for i in range(5):
    a.append(int(input()))
print(int(sum(a)/5))
print(statistics.median(a))
