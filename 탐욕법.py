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
    
    