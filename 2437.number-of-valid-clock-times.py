#
# @lc app=leetcode id=2437 lang=python3
#
# [2437] Number of Valid Clock Times
#

# @lc code=start
class Solution:
    '''
    Just try whatever combinations
    '''
    def validTime(self, time):
        if int(time[:2]) > 23 or int(time[3:]) > 59: return False
        return 0 <= int(time[:2]) * 60 + int(time[3:]) <= 23 * 60 + 59
     
    def countTime(self, time: str) -> int:
        pos = []
        pos.append('')
        for c in time:
            newPos = []
            if c != '?':
                for p in pos: newPos.append(p + c)
            else:
                for p in pos:
                    for i in range(10): newPos.append(p + str(i))
            pos = newPos
        result = 0
        for p in pos:
            if self.validTime(p): result += 1
        return result
# @lc code=end

