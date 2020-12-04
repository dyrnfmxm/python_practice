n = input()
s = 0
for i in n:
    i = int(i)
    s += i
    
if s % 7 == 4:
    print("suspect")
else:
    print("citizen")
