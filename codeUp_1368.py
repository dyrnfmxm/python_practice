a, b, d = input().split()
a = int(a)
b = int(b)

for i in range(a):
    if d == "R":
        print(" "*(a-i-1),end='')
        print("*"*b,end='')
    elif d == "L":
        print(" "*i,end='')
        print("*"*b,end='')
    print()
