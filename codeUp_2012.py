a,b = map(int,input().split())
count = 0
for i in range(a,b+1):
    i = str(i)
    for j in i:
        if j == '1':
            count += 1
print(count)

