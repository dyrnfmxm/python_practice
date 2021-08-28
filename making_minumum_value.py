def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(A)):
        #print(A[i]*B[i])
        answer += A[i] * B[i]
    

    return answer
