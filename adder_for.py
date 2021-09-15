def solution(a, b):
    if a == b:
        return a
    arr = []
    
    if a > b:
        a, b = b, a
    for i in range(a,b+1):
        arr.append(i)
    return sum(arr)
