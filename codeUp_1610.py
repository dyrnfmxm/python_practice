def mysubstr(s, a, b):
    print(s[a:a+b])

s = input()
a, b = map(int,input().split())

mysubstr(s, a, b)
