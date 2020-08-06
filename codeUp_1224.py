a, b, c, d = map(int, input().split())
s1 = a/b
s2 = c/d
#print(s1,s2)
if s1 > s2:
    print(">")
elif s1 == s2:
    print("=")
elif s1 < s2:
    print("<")
