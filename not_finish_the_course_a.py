def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    print(participant, completion)
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        elif i == len(completion)-1:
            return participant[i+1]
