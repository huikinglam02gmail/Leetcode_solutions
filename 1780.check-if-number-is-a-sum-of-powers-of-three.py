#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#

# @lc code=start
class Solution:
    '''
    return true if it is possible to represent n as the sum of distinct powers of three
    So we just need to go to the maximum power of 3 in which 3^i <= n < 3^(i + 1)
    And find out all the possible numbers
    '''
    def checkPowersOfThree(self, n: int) -> bool:
        thres = 0
        while pow(3, thres) <= n:
            thres += 1
        dp = [0 for i in range(1 << (thres))]
        for j in range(thres):
            dp[1 << j] = pow(3, j)
        for mask in range(1 << (thres)):
            binMask = bin(mask)[2:]
            if binMask[0] != '0':
                dp[mask] = dp[1 << (len(binMask) - 1)] + dp[mask - (1 << (len(binMask) - 1))]
        return n in set(dp)
        

# @lc code=end
