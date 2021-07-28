n = input()

rev_n = ''

for i in range(len(n)-1, -1, -1):
    if n[i] == 0:
        continue
    rev_n += n[i]

i = 0

for i in range(len(n)):
    if rev_n[i] == '0':
        continue
    elif int(rev_n[i]) > 0:
        rev_n = rev_n[i:]
        break
print(rev_n)
s = 0

for i in rev_n:
    s += int(i)

print(s)
