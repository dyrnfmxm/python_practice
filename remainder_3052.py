a = []
b = []
for i in range(10):
    a.append(int(input()))
#print(a)
for i in range(10):
    re = a[i] % 42
    b.append(re)
#print(b)
remove = list(set(b))
print(len(remove))
