a_card = list(map(int,input().split()))
b_card = list(map(int,input().split()))
a_win, b_win = 0, 0

for i in range(len(a_card)):
    if a_card[i] > b_card[i]:
        a_win += 1
    elif a_card[i] < b_card[i]:
        b_win += 1

if a_win > b_win:
    print('A')
elif a_win < b_win:
    print('B')
else:
    print('D')
