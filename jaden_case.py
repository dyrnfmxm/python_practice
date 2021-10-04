def solution(s):
    index = 0
    ss = ''
    
    for i in s:
        if i == " ":
            index = 0
        elif index == 0:
            i = i.upper()
            index += 1
        else:
            i = i.lower()
            index += 1
        ss += i
        
    return ss
