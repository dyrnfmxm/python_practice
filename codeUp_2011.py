a, b = map(int,input().split())

for i in range(a,b+1):
    count = 0
    i = str(i)
    for j in i:
        if j == '3' or j == '6' or j == '9':
            count += 1
    if count == 0:
        print(i)
    else:
        print('K'*count)
