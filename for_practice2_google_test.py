count = 0
for i in range(1,10000):
    s = str(i)
    for j in range(len(s)):
        #print(s[j])
        if int(s[j]) == 8:
            count += 1
print(count)

"""
count = 0
for i in range(1,10000):
    #자릿수 상관하지 않고 '8' = 문자로서의 8이 있는지 검사
    for j in str(i):
        if j == '8':
            count += 1
print(count)
"""
"""
google의 의도
8XXX = 000~999 - 1000개
X8XX = 1000개
XX8X = 1000개
XXX8 = 1000개
"""
