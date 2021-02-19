s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
s3 = list(map(int,input().split()))

s1.append(sum(s1))
s2.append(sum(s2))
s3.append(sum(s3))
score = []
for i in range(len(s1)):
    sum = s1[i] + s2[i] + s3[i]
    score.append(sum)

for i in range(len(s1)):
    print(s1[i],end=' ')
print()
for i in range(len(s2)):
    print(s2[i],end=' ')
print()
for i in range(len(s3)):
    print(s3[i],end=' ')
print()
for i in range(len(score)):
    print(score[i],end=' ')
