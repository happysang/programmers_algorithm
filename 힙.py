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
import heapq 
def solution(jobs):
    
    time, start, now = 0,-1,0
    heap = []
    res = 0
    while time < len(jobs):
        for x in jobs:
            if start < x[0] <= now:
                heapq.heappush(heap,[x[1],x[0]])

        if len(heap) >= 1:
            temp = heapq.heappop(heap)
            start = now
            now += temp[0]
            res += now - temp[1]
            time += 1
        else:
            now += 1
            
    return res // len(jobs)