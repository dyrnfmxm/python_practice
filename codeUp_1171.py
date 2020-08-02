a, b, c = map(int,input().split())
if b < 10 and c < 10:
    print('%d'"0"'%d'"00"'%d'%(a,b,c))
elif b < 10 and c < 100:
    print('%d'"0"'%d'"0"'%d'%(a,b,c))
elif b < 10:
    print('%d'"0"'%d%d'%(a,b,c))
elif c < 10:
    print('%d%d'"00"'%d'%(a,b,c))
elif c < 100:
    print('%d%d'"0"'%d'%(a,b,c))
else:
    print('%d%d%d'%(a,b,c))
