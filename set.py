blist = []
dlist = []
for i in range(3):
    b = int(input())
    blist.append(b)

for i in range(2):
    d = int(input())
    dlist.append(d)
    
print(min(blist)+min(dlist)-50)
