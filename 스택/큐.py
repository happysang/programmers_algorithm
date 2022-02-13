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