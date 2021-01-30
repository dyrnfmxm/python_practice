p = input()
if p[7] == '1' or p[7] == '2':
    print('19'+p[0]+p[1]+'/',end='')
else:
    print('20'+p[0]+p[1]+'/',end='')
print(p[2]+p[3]+'/'+p[4]+p[5],end=' ')
if p[7] == '1' or p[7] == '3':
    print('M')
else:
    print('F')
