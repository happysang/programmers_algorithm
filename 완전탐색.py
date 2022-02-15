### 모의고사
def solution(a):
    l1 = [1,2,3,4,5] * (len(a)//5) + [1,2,3,4,5][:len(a)%5]
    l2 = [2,1,2,3,2,4,2,5] * (len(a)//8) + [2,1,2,3,2,4,2,5][:len(a)%8]
    l3 = [3,3,1,1,2,2,4,4,5,5] * (len(a)//10) + [3,3,1,1,2,2,4,4,5,5][:len(a)%10]
    res = [[0,1],[0,2],[0,3]]
    for i in range(len(a)):
        if l1[i] == a[i]:
            res[0][0] += 1
        if l2[i] == a[i]:
            res[1][0] += 1
        if l3[i] == a[i]:
            res[2][0] += 1
    res.sort(key = lambda x:x[0], reverse=True)
    
    if res[0][0] == res[1][0]:
        if res[1][0] == res[2][0]:
            return [1,2,3]
        else:
            return [res[0][1],res[1][1]]
    else:
        return [res[0][1]]
            
                
### 소수찾기
def pnum(n):
    if n == 0 or n == 1:
        return []
    else:
        res = []
        tar = [False,False]+[True]*(n-1)
        for i in range(2,n+1):
            if tar[i]:
                res.append(i)
                for j in range(i*2,n+1,i):
                    tar[j] = False
        return res
                
from itertools import permutations
def solution(n):
    nums = []
    tar = set()
    for x in n:
        nums.append(x)
        tar.add(int(x))
        
    for i in range(2,len(nums)+1):
        temp = list(permutations(nums,i))
        for k in temp:
            tem = ''
            for t in range(len(k)):
                tem += k[t]
            tar.add(int(tem))
            
    lis = pnum(max(tar))
    res = 0
    for x in tar:
        if x in lis:
            res += 1
            
    return res


### 카펫
def solution(b, y):
    for k in range(1,y+1):
        if y%k == 0:
            if k*2 +  (y//k)*2 + 4 == b:
                return [(y//k)+2, k+2]