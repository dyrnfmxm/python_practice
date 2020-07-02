m = int(input())
n = int(input())
num_list = [] 
count = 0
for i in range(m,n):
    p = True
    for j in range(2,i):
        if i % j == 0:
            p = False
            break
    if p:
        num_list.append(i)
        count += 1
if count == 0:
    print('-1')
print(count)
print(num_list)
print(sum(num_list))
print(min(num_list))
