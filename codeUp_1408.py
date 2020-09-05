s = list(input())
for i in range(len(s)):
    s[i] = ord(s[i])
for i in range(len(s)):
    print(chr(s[i]+2),end='')
print()
for i in range(len(s)):
    print(chr((s[i]*7)%80+48),end='')
