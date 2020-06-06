a = []
for i in range(5):
    n = int(input())
    a.append(n)
    if a[i] < 40:
        a[i] = 40
    
avg = sum(a)/5
print(int(avg))
