n = int(input())
score_list = list(map(int,input().split()))

rank_list = sorted(score_list, reverse=True)

for i in score_list:
    for j in range(len(rank_list)):
        if i == rank_list[j]:
            print(i, j+1)
            break
