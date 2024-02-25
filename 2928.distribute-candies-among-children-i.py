#
# @lc app=leetcode id=2928 lang=python3
#
# [2928] Distribute Candies Among Children I
#

# @lc code=start
class Solution:
    '''
    brute force
    '''
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n:
                        result += 1
        return result
# @lc code=end

