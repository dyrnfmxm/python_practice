n = int(input())
sns_arr = []
s = 0
for i in range(n):
    sns_arr.append(input().split(','))

for i in sns_arr:
    s += len(i)-3
print('%.2f'%(s/n))
