t = list(map(int,input().split()))
a = 0
for i in range(len(t)):
    if t[i] <= 170:
        print("CRASH",t[i])
        break
    else:
        a += 1
if a == len(t):
    print("PASS")
