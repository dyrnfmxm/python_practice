t, s1, s2 = map(int,input().split())
if t < 90:
    s1 += 1
    s1 += int((89-t)/5)
if s1 == s2:
    print("same")
elif s1 > s2:
    print("win")
else:
    print("lose")
