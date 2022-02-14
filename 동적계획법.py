### 정수 삼각형
def solution(t):
    t = list(reversed(t))

    for i in range(len(t)):
        for j in range(len(t[i])-1):
            if t[i][j] >= t[i][j+1]:
                t[i+1][j] += t[i][j]
            else:
                t[i+1][j] += t[i][j+1]
                
    return t[-1][-1]