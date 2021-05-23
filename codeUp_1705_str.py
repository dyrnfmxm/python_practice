n = input()
answer = ''

if n[0] == '3' or n[0] == '6' or n[0] == '9':
    answer = answer + 'K'
if len(n) >= 2:
    if n[1] == '3' or n[1] == '6' or n[1] == '9':
        answer = answer + 'K'
if len(n) >= 3:
    if n[2] == '3' or n[2] == '6' or n[2] == '9':
        answer = answer + 'K'

if answer != '':
    print(answer)
else:
    print(n)
