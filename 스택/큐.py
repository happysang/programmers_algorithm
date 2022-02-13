### 기능개발
def solution(p, s):
    
    val = []
    for i in range(len(p)):
        if (100-p[i]) // s[i] == (100-p[i]) / s[i]:
            val.append((100-p[i]) // s[i])
        else:
            val.append((100-p[i]) // s[i] + 1)
    
    answer = []
    cnt = 1
    m = val[0]
    for i in range(1,len(val)):
        if m >= val[i]:
            cnt += 1
        else:
            answer.append(cnt)
            m = val[i]
            cnt = 1
    answer.append(cnt)
    return answer


###프린터
from collections import deque
def solution(p, l):
    val = []
    for i in range(len(p)):
        val.append((p[i],i))
    val = deque(val)
    
    cnt = 0
    while(val):
        if val[0][0] == max(p):
            if l == val[0][1]:
                cnt += 1
                return cnt
            else:
                p.remove(val[0][0])
                val.popleft()
                cnt += 1
        else:
            val.append(val.popleft())