t = input()
ut = t.upper()
f = w = 0
#print(t2.count(chr(65)))
for i in range(65,91):
    if f < ut.count(chr(i)):
        f = ut.count(chr(i))
        w = chr(i)
    elif f == ut.count(chr(i)):
        w = "?"
print(w)
