def upper_bound(num_list, number):
    for i in range(len(num_list)):
        if number < num_list[i]:
            #print(num_list[i])
            return i+1
            break
    return len(num_list)+1

n = int(input())
ki = list(map(int,input().split()))
k = int(input())

print(upper_bound(ki, k))
