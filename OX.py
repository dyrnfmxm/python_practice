n = int(input())
for i in range(n):
    arr = list(input())
    score = a = 0
    for j in range(len(arr)):
        
        #print(arr[j])
        if arr[j] == 'O':
            a +=1
            score += a
        else:
            a = 0
    print(score)
