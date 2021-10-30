def solution(array, commands):

    answer = []

    for i in commands:

        a, b, c = i[0]-1, i[1], i[2]-1

        arr = array[a:b]

        arr.sort()

        

        answer.append(arr[c])

        
    return answer

