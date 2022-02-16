### k번째수
def solution(a, c):
    res = []
    for x in c:
        res.append(sorted(a[x[0]-1:x[1]])[x[2]-1])
    return res