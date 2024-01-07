#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
class Solution:
    '''
    0 <= start, goal <= 10^9 < 2 ^ 30
    We just need to represent start and goal in binary and count how many digits needs to be flipped.
    '''

    def minBitFlips(self, start: int, goal: int) -> int:
        binStart = bin(start)[2:].zfill(30)
        binGoal = bin(goal)[2:].zfill(30)
        result = 0
        for i in range(30):
            if binStart[i] != binGoal[i]: result += 1
        return result
# @lc code=end

