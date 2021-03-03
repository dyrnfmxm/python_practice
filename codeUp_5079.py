n = int(input())
vote = input()
a = b = 0

for i in vote:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1

if a > b :
    print("A")
elif b > a :
    print("B")
elif a == b:
    print("Tie")
