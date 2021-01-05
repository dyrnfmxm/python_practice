n = int(input())
a = list(map(int,input().split()))

a2 = sorted(a)
a3 = reversed(a2)

if a == a2:
    print("오름차순")
elif a == list(a3):
    print("내림차순")
else:
    print("섞임")
