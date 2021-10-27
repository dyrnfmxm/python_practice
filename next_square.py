def solution(n):
    i = 1
    
    while True:
        
        if n < i*i:
            return -1
        elif n == i * i:
            return (i+1)**2
        i += 1
