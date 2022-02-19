### 타겟 넘버
global cnt
cnt = 0

def dfs(k,i,res,nums,tar):
    global cnt
    if k == len(nums)-1 and res == tar:
        cnt += 1
        
    for t in range(2):
        if k != len(nums)-1:
            dfs(k+1,i+t,res+nums[k][i+t],nums,tar)

def solution(numbers, tar):
    numbers.append(0)
    nums = []
    temp = []
    for x in range(len(numbers)):
        for i in range(x+1):
            temp.append(numbers[x])
            temp.append(-numbers[x])
        nums.append(temp)
        temp = []
    
    dfs(0,0,0,nums,tar)
    return cnt


### 네트워크
global res
temp = []
res = 0
def bfs(lis):
    global res
    for i in range(len(lis)):
        if lis[i][i] == 1:
            res += 1
            temp.append(i)
        else:
            continue
        
        while(temp):
            tar = temp.pop(0)
            for j in range(len(lis[tar])):
                lis[tar][tar] == 0
                if lis[tar][j] == 1:
                    lis[j][tar] = 0
                    temp.append(j)

def solution(n, computers):
    bfs(computers)
    return res
    