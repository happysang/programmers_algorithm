### k번째 수
def solution(a, c):
    res = []
    for x in c:
        res.append(sorted(a[x[0]-1:x[1]])[x[2]-1])
    return res

### 가장 큰 수
def solution(n):
    nums = sorted(list(map(str,n)),reverse=True)
    tar = []
    temp = [nums[0]]
    for i in range(len(nums)):
        if nums[i][0] == nums[i-1][0]:
            temp.append(nums[i])
            
    print(nums)
    answer = ''
    for i in nums:
        answer += i   
    return answer