#
# @lc app=leetcode id=2224 lang=python3
#
# [2224] Minimum Number of Operations to Convert Time
#

# @lc code=start
class Solution:
    '''
    Convert correct and current to the minute system
    Then increment current in 60, 15, 5 and 1 minutes
    '''
    def convertTime(self, current: str, correct: str) -> int:
        correctTime = int(correct[:2]) * 60 + int(correct[3:])
        currentTime = int(current[:2]) * 60 + int(current[3:])
        result = 0
        for increment in [60, 15, 5, 1]:
            inc = (correctTime - currentTime) // increment
            currentTime += inc * increment
            result += inc
        return result
# @lc code=end

