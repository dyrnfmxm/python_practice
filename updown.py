import random

number = random.randint(1,100)
tries = 0

print("숫자 맞추기")
while tries < 10:
    n = int(input("숫자 입력"))

    tries = tries+1

    if n<number:
        print("UP")

    elif n>number:
        print("DOWN")
    else:
        break

if n==number:

    print("시도횟수 : ", tries)
else:
    print("정답은 : ", number)
