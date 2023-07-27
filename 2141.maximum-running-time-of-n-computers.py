#
# @lc app=leetcode id=2141 lang=python3
#
# [2141] Maximum Running Time of N Computers
#

# @lc code=start
from typing import List


class Solution:
    '''
    First sort batteries. 
    Then we notice if batteries[-1] >= sum(batteries) // n, we can use the last battery throughout for one of the computers. The problem becomes that on n - 1 computers and batteries[:-1] available. As shown in Example 1, if 3 = batteries[-1] < sum(batteries) // n = 4, the maximum time we can go for is sum(batteries // n)
    '''
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        S = sum(batteries)
        while batteries[-1] >  S // n:
            n -= 1
            S -= batteries.pop()
        return S // n
        
# @lc code=end

