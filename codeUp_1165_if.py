time, score = map(int,input().split())
if time < 90:
    score += 1
    s = 90-time-1
#    print(s)
    s2 = int(s/5)
#    print(s2)
    print(s2+score)
