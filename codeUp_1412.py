n = input()
c = [0]*26
for i in range(len(n)):
    for j in range(97, 123):
        if ord(n[i]) == j:
            c[j-97] += 1
for i in range(len(c)):
    print("%c:%d"%(chr(i+97),c[i]))
