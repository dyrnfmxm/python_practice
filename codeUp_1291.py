a, b, c = map(int,input().split())
arr = []    # 공약수 저장을 위한 배열
i = 1

while i <= min(a,b,c):  # 셋 중 가장 낮은 값까지
    if a % i == 0 and b % i == 0 and c % i == 0:    # 나누면서 공약수 구하기
        arr.append(i)   # 배열에 삽입
    i += 1 

print(max(arr))     # 공약수 중 가장 큰 값 출력
