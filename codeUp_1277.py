n = int(input())
arr = list(map(int,input().split()))
if n == 1:
    print('%d %d %d'%(arr[0], arr[0], arr[0]))
else :
    print('%d %d %d'%(arr[0], arr[int(n/2)], arr[n-1]))
