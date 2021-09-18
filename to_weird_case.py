def solution(s):
    index = 0
    ss = ''
    for i in str(s):
        if i == ' ':
            index = 0
        elif index % 2 == 0:
            i = i.upper()
            index += 1
        elif index % 2 == 1:
            i = i.lower()
            index += 1
        ss += i
    return ss
