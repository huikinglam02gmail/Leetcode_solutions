#
# @lc app=leetcode id=2162 lang=python3
#
# [2162] Minimum Cost to Set Cooking Time
#

# @lc code=start
class Solution:
    '''
    1 <= targetSeconds <= 6039, 6039 = 99 * 60 + 99
    so given targetSeconds, possible sequencing to push = str(targetSecond // 60) + str((targetSecond - targetSecond // 60 * 60))
    if targetSeconds >= 100, an alternative is str(targetSecond // 60 - 1) + str(targetSecond - (targetSecond // 60 - 1)* 60)
    the condition to hold is targetSecond - (targetSecond // 60 - 1)* 60 <= 99
    '''
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        candidates =  [str(targetSeconds // 60) + str(targetSeconds - targetSeconds // 60 * 60).zfill(2)]
        if len(candidates[0]) > 4: candidates.pop()
        if targetSeconds // 60 > 0 and targetSeconds - (targetSeconds // 60 - 1)* 60 <= 99: candidates.append(str(targetSeconds // 60 - 1) + str(targetSeconds - (targetSeconds // 60 - 1)* 60).zfill(2))
        result = float("inf")
        for candidate in candidates:
            last = startAt
            current = 0
            for c in str(int(candidate)):
                if int(c) != last: current += moveCost
                current += pushCost
                last = int(c)
            result = min(result, current)
        return result
# @lc code=end

