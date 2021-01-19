n = int(input())
sns_arr = []

for i in range(n):
    sns_arr.append(input().split(','))

p = input()

for i in sns_arr:
    if i[0] == p:
        for j in range(3,len(i)):
            print(i[j])
