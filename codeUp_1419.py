a = input()
count = 0
for i in range(len(a)-3):
    if a[i]+a[i+1]+a[i+2]+a[i+3] == 'love':
        count += 1
print(count)
