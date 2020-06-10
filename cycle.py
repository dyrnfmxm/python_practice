n = int(input())
m = s = count = 0
t = n
while True:
    m = ((t%10)*10) + ((int((t/10))+(t%10))%10)
    #print((t%10)*10)
    #print(((int((t/10))+(t%10))%10))
    count += 1
    #print(m)
    if n == m:
        break
    t = m
print(count)
