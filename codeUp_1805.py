n = int(input())
dict = {}

for i in range(n):
    a, b = map(int,input().split())
    dict[a] = b

sdict = sorted(dict.items())


for i in sdict:
    print(i[0], i[1])
