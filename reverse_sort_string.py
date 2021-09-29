def solution(s):
    arr = []
    for i in s:
        arr.append(ord(i))
    arr.sort(reverse=True)
    
    answer = []
    for i in arr:
        answer.append(chr(i))
         
    return ''.join(answer)
