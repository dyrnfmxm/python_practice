a = list(input())
c1 = c2 = 0
for i in range(len(a)):
    if a[i] == "(":
        c1 += 1
    elif a[i] == ")":
        c2 += 1
print(c1, c2)
