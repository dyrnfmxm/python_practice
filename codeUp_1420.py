import statistics

n = int(input())
a = list()
s = list()
for i in range(n):
    a.append(input().split())
for i in range(len(a)):
    s.append(int(a[i][1]))
s.sort(reverse=True)
#print(s)
for i in range(n):
    if int(a[i][1]) == s[2]:
        print(a[i][0])
