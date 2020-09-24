n = int(input())
a1 = list(map(int,input().split()))
a2 = []
i = 0

while i < len(a1):
    if a1[i] > a1[i+1]:
        a2.append(a1[i+1])
        i += 2
    elif a1[i] < a1[i+1]:
        a2.append(a1[i])
        i += 2

for i in range(len(a2)):
    print(a2[i],end=' ')
