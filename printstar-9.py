n = int(input())
for i in range(1,n+1):
    print(" "*(i-1),end='')
    print("*"*((2*n)-(2*i-1)))
    if i >= n:
        for i in range(n-1, 0, -1):
            print(" "*(i-1),end='')
            print("*"*((2*n)-(2*i-1)))    
