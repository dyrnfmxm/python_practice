n = int(input())

if n == 11 or n == 12 or n == 13:
    print('%dth'%n)
elif n%10 == 1:
    print('%dst'%n)
elif n%10 == 2:
    print('%dnd'%n)
elif n%10 == 3:
    print('%drd'%n)
else:
    print('%dth'%n)
