a, b = map(int,input().split())
if a%2 == 0:
    print("짝수+",end='')
else:
    print("홀수+",end='')
if b%2 == 0:
    print("짝수=",end='')
else:
    print("홀수=",end='')
if (a+b)%2 == 0:
    print("짝수")
else:
    print("홀수")
