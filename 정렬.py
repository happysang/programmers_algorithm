### k번째 수
def solution(a, c):
    res = []
    for x in c:
        res.append(sorted(a[x[0]-1:x[1]])[x[2]-1])
    return res

### 가장 큰 수
def solution(n):
    return str(int(''.join(sorted(list(map(str,n)), key = lambda x : x*3, reverse = True))))