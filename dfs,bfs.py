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