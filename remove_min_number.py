def solution(arr):
    answer = arr
    
    answer.remove(min(arr))
    
    if len(answer) == 0:
        return [-1]
    else:
        return answer
