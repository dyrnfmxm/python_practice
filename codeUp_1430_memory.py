n = int(input())
q1 = list(map(int,input().split()))
m = int(input())
q2 = list(map(int,input().split()))
c = [0]*m

for i in range(m):
    for j in range(n):
        if q2[i] == q1[j]:
            c[i] = 1

for i in range(len(c)):
    print(c[i],end=' ')
