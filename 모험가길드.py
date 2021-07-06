n = int(input())
arr = list(map(int,input().split()))

arr.sort()

count = 0 # 총 그룹의 수
guild = 0 # 현재 그룹에 포함된 모험가의 수

for i in arr:   # 공포도를 낮은 것부터 하나 씩 확인하며
    guild += 1  # 현재 그룹에 해당 모험가 포함
    if i == guild:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면
        count += 1  # 그룹 결성 그룹 수 증가
        guild = 0   # 현재 그룹에 포함된 인원 초기화 

print(count)
