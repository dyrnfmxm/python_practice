password = input()
number = input()
pass_num = []

for i in number:
    if i == ' ':
        pass_num.append(' ')
    for j in range(len(password)):
        if i == password[j]:
            pass_num.append(j)

for i in pass_num:
    print(i,end='')
