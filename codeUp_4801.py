k, n, m = map(int,input().split())

money = k * n

if m > money:
    print('0')
else:
    print(money - m)
