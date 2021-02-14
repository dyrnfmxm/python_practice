a = list(map(int,input().split()))
odd = []
even = []

for i in a:
    if i%2 == 0:
        even.append(i)
    elif i%2 == 1:
        odd.append(i)

if len(even) == 0:
    print(max(odd))
elif len(odd) == 0:
    print(max(even))
else:
    print(max(odd), max(even))
