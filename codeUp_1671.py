a, b = map(int,input().split())

if a == 0:
    if b == 0:
        print("tie")
    elif b == 1:
        print("win")
    elif b == 2:
        print("lose")
        
elif a == 1:
    if b == 0:
        print("lose")
    elif b == 1:
        print("tie")
    elif b == 2:
        print("win")
        
if a == 2:
    if b == 0:
        print("win")
    elif b == 1:
        print("lose")
    elif b == 2:
        print("tie")
