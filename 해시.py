### 완주하지 못한 선수
#내 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i] == participant[i]:
            continue
        else:
            return participant[i]
    return participant[-1]

# 좋은 풀이
from collections import Counter

def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]



### 전화번호 목록
def solution(phone_book):
    if len(phone_book) == 1:
        return True
    else:
        phone_book.sort()
        for i in range(len(phone_book)-1):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False
        return True



### 위장
from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)
    for x in clothes:
        dic[x[-1]] += 1
    
    res = 1
    for x in dic.values():
        res *= (x+1) 
        
    return res-1



###베스트 앨범
def solution(g, p):
    from collections import defaultdict
    dic = defaultdict(list)
    
    for i in range(len(g)):
        if len(dic[g[i]]) == 0:
            dic[g[i]].append(0)
        dic[g[i]].append([p[i],i])
        dic[g[i]][0] += p[i]
    
    tar = list(dic.values())
    tar.sort(key=lambda x:-x[0])
    
    print(tar)
    res = []
    for x in tar:
        tarx = x[1:]
        tarx.sort(key = lambda x:(-x[0], x[1]))
        if len(tarx) == 1:
            res.append(tarx[0][-1])
        else:
            res.append(tarx[0][1])
            res.append(tarx[1][1])
    return res
        
        