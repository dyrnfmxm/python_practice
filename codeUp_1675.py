s = list(input())
for i in range(len(s)):
    if s[i] == ' ':
        print(s[i],end='')
    else:
        s[i] = ord(s[i])
        s[i] = s[i] -3
        if s[i] < 97:
            s[i] = s[i] + 26
            s[i] = chr(s[i])
        else:
            s[i] = chr(s[i])
        print(s[i],end='')
