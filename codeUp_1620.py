n = int(input())
while True:         # 한 자릿수가 될 때 까지 반복
    s = 0           
    for i in n:     
        s += int(i) # 한 자릿수씩 s에 합산
        n = str(s)  # 다시 문자열로 변환 후 재 연산 준비
#    print(s)
    if s/10 < 1:    # 한 자릿수가 되면
        print(s)    # 현재 s값을 출력하고 반복문 종료
        break
