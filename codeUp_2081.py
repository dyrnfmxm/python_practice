a = []
for i in range(9):
    a.append(int(input()))

for i in range(len(a)):
    if a[i] == max(a):
        print(a[i])
        print(i+1)
