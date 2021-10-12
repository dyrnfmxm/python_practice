def solution(n):
    
    a = str(n)
    arr = []
    
    for i in range(len(a)):
        arr.append(a[i])
    arr.sort(reverse = True)
    answer = ''
    
    for i in arr:
        answer += i
    return int(answer)
