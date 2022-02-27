### 가장 먼 노드
from collections import defaultdict
def solution(n, edge):
    visit = [1] * (n+1)
    dic = defaultdict(list)
    for x in edge:
        dic[x[0]].append(x[1])
        dic[x[1]].append(x[0])
    
    temp = dic[1]
    visit[1] = 0
    
    for x in temp:
        visit[x] = 0

    while True:
        print(temp)
        lis = []
        for x in temp:
            for k in dic[x]:
                if visit[k] != 0:
                    lis.append(k)
                    visit[k] = 0
                
        if len(lis) == 0:
            return len(temp)
        else:
            temp = lis
                
            
            