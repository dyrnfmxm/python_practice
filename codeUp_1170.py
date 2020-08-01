a, b, c = map(int,input().split())
if c < 10:
    print('%d%d0%d'%(a,b,c))
else:
    print('%d%d%d'%(a,b,c))
