n = int(input())
p = []
nList = []
for i in range(2,n):
    if n%i == 0:
        nList.append(i)
#print(nList)
for i in nList:
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count+=1
#    print(count)
    if count == 0:
        p.append(i)

if len(p) == 0:
    print("wrong number")
elif min(p) * max(p) != n:
    print("wrong number")
else:
    print(min(p),max(p))
