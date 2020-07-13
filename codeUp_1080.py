n = int(input())
i = 0
s = 0
while True:
    if s >= n:
        print(i)
        break
    else:
        i += 1
        s += i
        #print(i,s)
