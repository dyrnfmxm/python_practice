a = []
a2 = []
for i in range(7):
    a.append(int(input())

for i in a:
    if i % 2 == 1:
        a2.append(i)

if len(a2) == 0:
    print(-1)
else:
    print(sum(a2))
    print(min(a2))