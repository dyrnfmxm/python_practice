def solution(s):
    arr = list(s)
    
    return ''.join(sorted(arr, reverse=True))
