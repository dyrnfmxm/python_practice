def rank(num_list, number):
    new_list = sorted(num_list, reverse = True)

    for i in range(len(new_list)):
        if number == new_list[i]:
            return i+1
        

n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    print(arr[i], rank(arr,arr[i]))
