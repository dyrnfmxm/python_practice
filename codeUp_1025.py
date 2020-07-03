import math
n = input()
for i in range(len(n)):
    pow = int(math.pow(10,len(n)-(i+1)))
    #print(pow)
    result = (int(n[i]))*pow
    print("[%d]"%result)
