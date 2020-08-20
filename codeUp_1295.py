s = list(input())
for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        print(s[i].lower(),end='')
    elif 'a' <= s[i] <= 'z':
        print(s[i].upper(),end='')
    else:
        print(s[i],end='')
