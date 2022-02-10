##키패드 누르기
nums = [[4,2],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
def solution(numbers, hand):
    res = ""
    lp,rp = [4,1],[4,3]
    for x in numbers:
        if x == 1 or x == 4 or x == 7:
            res += "L"
            lp = nums[x]
        elif x == 3 or x == 6 or x == 9:
            res += "R"
            rp = nums[x]
        else:
            if abs(nums[x][0]-lp[0]) + abs(nums[x][1]-lp[1]) < abs(nums[x][0]-rp[0]) + abs(nums[x][1]-rp[1]):
                res += "L"
                lp = nums[x]
            elif abs(nums[x][0]-lp[0]) + abs(nums[x][1]-lp[1]) > abs(nums[x][0]-rp[0]) + abs(nums[x][1]-rp[1]):
                res += "R"
                rp = nums[x]
            else:
                if hand == "right":
                    res += "R"
                    rp = nums[x]
                else:
                    res += "L"
                    lp = nums[x]
    return res