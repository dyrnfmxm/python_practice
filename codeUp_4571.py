m = int(input())
n = int(input())

i = 1
arr = []

while True:
    result = 0

    result = i * i
    #print(result)
    arr.append(result)

    i += 1

    if result >= 10000:
        break

result_arr = []

for i in range(m, n+1):
    if i in arr:
        result_arr.append(i)

print(sum(result_arr))
print(min(result_arr))
