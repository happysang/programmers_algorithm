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


### 등굣길
def solution(m, n, p):
    way = [[0 for _ in range(m+1)] for _ in range(n+1)]
    way[0][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in p:
                way[i][j] = 0
            else:
                way[i][j] = (way[i - 1][j] + way[i][j - 1]) % 1000000007
                
    return way[-1][-1]