n = int(input())
a = list(map(int,input().split()))

print(a.index(max(a))+1,':',max(a))
print(a.index(min(a))+1,':',min(a))
