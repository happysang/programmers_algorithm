##### 완주하지 못한 선수
##내 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i] == participant[i]:
            continue
        else:
            return participant[i]
    return participant[-1]

