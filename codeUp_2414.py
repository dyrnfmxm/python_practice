n = int(input())
sns_arr = []
s = 0
for i in range(n):
    sns_arr.append(input().split(','))
p = input()

for i in sns_arr:
    if i[0] == p:
        print(i[2])
