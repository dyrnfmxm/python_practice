def max_number(number_list, start_index, end_index):
    check_list = number_list[start_index-1:end_index]
    max_num = max(check_list)
    #print(max_num)
    #print(number_list)
    
    for i in range(len(number_list)):
        if number_list[i] == max_num:
            print(i+1)
            break
    
n = int(input())
num_list = list(map(int, input().split()))
start, end = map(int,input().split())

max_number(num_list, start, end)
