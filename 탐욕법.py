### 체육복
def solution(n, lost, reserve):
    stud = [1] * (n+1)
    
    for i,j in (lost,reserve):
        stud[i] -= 1
        
    for i in reserve:
        stud[i] += 1
    
    
    for i in sorted(reserve):
        if stud[i] == 1:
            continue
        if i == 1:
            if stud[i+1] == 0:
                stud[i+1] = 1
        elif i == n:
            if stud[i-1] == 0:
                stud[i-1] = 1
        else:
            if stud[i-1] == 0:
                stud[i-1] = 1
            elif stud[i+1] == 0:
                stud[i+1] = 1

    print(stud)
    return len([x for x in stud if x != 0])-1
    
    
    ### 조이스틱
    def solution(name):
        res1 = -1
    tar1 = ''
    for x in name:
        if x != 'A':
            tar1 += x
    temp1 = ''
    
    for x in range(len(name)):
        res1 += 1
        if temp1 == tar1:
            break
        if ord(name[x]) <= 77:
            res1 += (ord(name[x])-65)
        else:
            res1 += (90-ord(name[x])+1)
        temp1 += name[x]
            
    
    res2 = -1
    tar2 = ''
    name = name[0]+name[len(name):0:-1]
    for x in name:
        if x != 'A':
            tar2 += x
    temp2 = ''
    
    for x in range(len(name)):
        res2 += 1
        if temp2 == tar2:
            break
        if ord(name[x]) <= 77:
            res2 += (ord(name[x])-65)
        else:
            res2 += (90-ord(name[x])+1)
        temp2 += name[x]

    return min(res1, res2)
    
    
    ## 큰 수 만들기
    
    def solution(number, k):
        val = []
    for x in number:
        val.append(int(x))
    
    print(val)
    i = 0
    for _ in range(k):
        print("!!!")
        while True:
            if val[i] > val[i+1]:
                del val[i+1]
                break
            elif val[i] < val[i+1]:
                del val[i]
                break
            else:
                i+=1
        print(val)
            
        return ''.join(list(map(str,val)))