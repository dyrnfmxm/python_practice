n = int(input())
sns_arr = []
f = m = 0

for i in range(n):
    sns_arr.append(input().split(','))      // sns_arr로 입력받기

p = input()
fList = []                                  

for i in sns_arr:
    if i[0] == p:
        for j in range(3,len(i)):
            fList.append(i[j])              // 해당 인물의 친구들을 리스트로 저장

for i in fList:
    for j in sns_arr:
        if i == j[0]:                       // 2차원 배열로 이름이 일치할시
            if j[1] == 'M':
                m += 1
            elif j[1] == 'F':
                f += 1                      // 성별을 검사하여 숫자 증가
print(m)
print(f)
