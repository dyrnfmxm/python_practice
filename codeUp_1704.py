n1, n2 = input().split()

age = n1[:2]
sex = n2[0]

if n2[0] == '1' or n2[0] == '3':
    sex = 'M'
else:
    sex = 'F'

if n1[0] == '0' or n1[0] == '1':
    if n2[0] == '1' or n2[0] == '2':
        age = '19'+age
    else:
        age = '20'+age
else:
    if n2[0] == '1' or n2[0] == '2':
        age = '19'+age
    else:
        age = '20'+age

age = 2012 - int(age) + 1

print(age, sex)
