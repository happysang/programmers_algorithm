### 모의 고사
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
            
                
