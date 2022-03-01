### 더 맵게
import heapq
def solution(s, k):
    heapq.heapify(s)

    cnt = 0
    while s[0] < k:
        a = heapq.heappop(s)
        b = heapq.heappop(s)
        temp = a + b*2
        heapq.heappush(s, temp)
        if len(s) == 1 and s[0] < k:
            return -1
        cnt += 1
    
    return cnt


### 디스크 컨트롤러
import heapq as hp
def solution(jobs):
    nums = []
    for x in jobs:
        hp.heappush(nums, [x[1],x[0]])
    
    print(nums)
    
    res = 0
    for _ in range(len(jobs)):
        res += hp.heappop(nums)[1]
        print(res)
        