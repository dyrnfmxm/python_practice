result = ''
n = int(input())
for i in range(2,n):
    result += ("\n{}단!\n".format(i))
    for j in range(1,21):
        result += ("{} X {} = {}\n".format(i,j,i*j))
print(result)
