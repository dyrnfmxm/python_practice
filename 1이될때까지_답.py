n, k = map(int,input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k     # n이 k로 나누어 떨어지는 가장 가까운 수 찾는 법
    result += (n - target)  # 한 번에 -1 횟수 더하기
    n = target              # n이 나누어 떨어질 수 있도록 수 대입

    if n < k:               # N을 K로 더이상 나눌 수 없을 때 반복문 탈출
        braek

    result += 1             
    n //= k

result += (n-1)             # 마지막으로 남은 수에 대하여 1씩 빼
print(result)
