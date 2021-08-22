def solution(price, money, count):
    answer = 0
    total_price = 0
    
    for i in range(count+1):
        total_price += i * price
        
    answer = total_price - money
    return 0 if answer <= 0 else answer
