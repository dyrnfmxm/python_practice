t = int(input())
for i in range(t):
    #p = []
    s, r = input().split()
    s = int(s)
    #print(s, r)
    #p = r
    #print(p)
    for i in range(len(r)):
        print(r[i]*s,end='')
    print()
