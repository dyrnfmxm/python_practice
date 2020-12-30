p = []
j = []
for i in range(3):
    p.append(int(input()))
for i in range(2):
    j.append(int(input()))
s = min(p)+min(j)
print(round((s*1.1),1))
    
