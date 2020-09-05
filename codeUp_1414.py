s = input()
cCount = ccCount = 0
for i in range(len(s)):
    if s[i] == 'c' or s[i] == 'C':
        cCount +=1
    if i+1 < len(s):
        if s[i]+s[i+1] == 'cc' or s[i]+s[i+1] == 'cC' or s[i]+s[i+1] == 'Cc' or s[i]+s[i+1] == 'CC':
            ccCount +=1
print(cCount)
print(ccCount)
