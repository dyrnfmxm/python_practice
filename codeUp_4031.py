a = list(map(int,input().split()))
odd = even = 0
for i in range(len(a)):
    if a[i]%2 == 0:
        if a[i] > even:
            even = a[i]
    elif a[i]%2 == 1:
        if a[i] > odd:
            odd = a[i]

print(odd+even)
