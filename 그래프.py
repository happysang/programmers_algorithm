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
                
            
### 순위
from collections import defaultdict

def solution(n, res):
    win = defaultdict(list)
    lose = defaultdict(list)
    
    for x in res:
        win[x[0]].append(x[1])
        lose[x[1]].append(x[0])
    
    for _ in range(n):
        for x in list(win.keys()):
            for k in win[x]:
                win[x] = list( set(win[x]) | set(win[k]) )

        for x in list(lose.keys()):
            for k in lose[x]:
                lose[x] = list( set(lose[x]) | set(lose[k]) )
    
    cnt = 0
    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            cnt += 1
            
    return cnt