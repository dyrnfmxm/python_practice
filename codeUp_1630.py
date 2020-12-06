n = int(input())
ws = []
for i in range(n):
    ws.append(input())

for i in range(n):
    print(ws[i])
    if i < n-1:
        print("AMOLED")
