def num_location(num_list, number):
    for n in num_list:
        if n == number:
            return num_list.index(n) + 1
            break
    return -1
        
    

n = int(input())
num_list = list(map(int,input().split()))
number = int(input())
print(num_location(num_list, number))
