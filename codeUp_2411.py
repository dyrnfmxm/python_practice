n = int(input())
sns_arr = []
f = m = 0
for i in range(n):
    sns_arr.append(input().split(','))

for i in sns_arr:
    if i[1] == 'F':
        f += 1
    elif i[1] == 'M':
        m += 1
print(m)
print(f)
