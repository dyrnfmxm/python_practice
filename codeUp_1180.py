n = int(input())
nn = int(n/10)+((n%10)*10)
r = nn*2
if r >= 100:
    r = r%100
print(r)
if r <= 50:
    print("GOOD")
else:
    print("OH MY GOD")
