arr = list(map(int,input().split()))

n = arr[0]

ch_index = n//2
num_arr = arr[1:]

rev_arr = sorted(num_arr, reverse = True )

rev_arr[0], rev_arr[ch_index] = rev_arr[ch_index], rev_arr[0]

for i in rev_arr:
    print(i, end=' ')
