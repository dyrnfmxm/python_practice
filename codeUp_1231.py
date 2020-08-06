a = input()
o = 0
n1 = []
n2 = []
for i in range(len(a)):
    if a[i] == '+' or a[i] == '-' or a[i] == '*' or a[i] == '/':
        o = i
#        print("o =", a[i])
        break
for i in range(o):
#    print(a[i])
    n1.append(a[i])
#print(n1)
j1 = "".join(n1)
#print(j1)
j1 = int(j1)
for i in range(o+1,len(a)):
#    print(a[i])
    n2.append(a[i])
#print(n2)
j2 = "".join(n2)
#print(j2)
j2 = int(j2)
if a[o] == "+":
    print(j1+j2)
elif a[o] == "-":
    print(j1-j2)
elif a[o] == "*":
    print(j1*j2)
elif a[o] == "/":
    print('%.2f'%(j1/j2))
