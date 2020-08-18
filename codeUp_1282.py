n = int(input())
tList = []
t = 1
while True:
    if t**2 <= n:
        tList.append(t)
        t += 1
    else:
        break
print(tList)
k = (n - (max(tList)**2))
print(k, t-1)
