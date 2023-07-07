#
# @lc app=leetcode id=1798 lang=python3
#
# [1798] Maximum Number of Consecutive Values You Can Make
#

# @lc code=start
class Solution:
    '''
    Sort coins
    [1,4,10,3,1] -> [1,1,3,4,10]
    From zero, we are first given 1. So sum up to 1 is possible
    Given another 1, we are achieve up to 1 (num) + 1 (possible) = 2
    Given 3, which is possible + 1, we have no gaps in between. So possible = 3 + 2 = 5
    '''
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        possible = 0
        for coin in coins:
            if possible + 1 < coin:
                break
            else:
                possible += coin
        return possible + 1
# @lc code=end

