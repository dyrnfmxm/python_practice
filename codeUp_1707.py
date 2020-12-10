score = list(map(int,input().split()))
avg_score = sum(score)/len(score)
print(avg_score)

u_score = 0
d_score = 0

for i in score:
    if i >= avg_score:
        u_score += 1
    elif i < avg_score:
        d_score += 1
print(u_score, d_score)
