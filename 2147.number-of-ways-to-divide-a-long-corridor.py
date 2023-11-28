#
# @lc app=leetcode id=2147 lang=python3
#
# [2147] Number of Ways to Divide a Long Corridor
#

# @lc code=start
class Solution:
    '''
    First run through and count the number of S. If count % 2 > 0: return 0
    Next go through corridor again and when note the positions where count[i] % 2 == 1 and count[j] % 2 == 0
    If j < i, the number of possibilities to put the bar is j - i
    Multiply all these together
    '''
    def numberOfWays(self, corridor: str) -> int:
        MOD, n = pow(10, 9) + 7, len(corridor)
        l, r, countS, result = n, n, 0, 1
        for i in range(n):
            if corridor[i] == 'S': 
                countS += 1
                if countS % 2: 
                    r = i
                else: 
                    l = i
                if l < r:
                    result *= r - l
                    result %= MOD
        if countS % 2: return 0
        else: return result
# @lc code=end

