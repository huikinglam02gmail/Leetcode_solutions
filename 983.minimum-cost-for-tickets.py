#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
import bisect
from functools import lru_cache
from typing import List


class Solution:
    '''
    A DP problem clearly. We would buy the first ticket on days[0], then we binary search for the day in days in which the ticket cannot cover. The search ends when days are empty. To allow for memo, we use index i in which 0 <= i < n to identify the current uncovered day    
    '''
    @lru_cache(None)
    def dfs(self, i):
        if i == self.n: return 0
        result = float('inf')
        result = min(result, self.costs[0] + self.dfs(i + 1))
        index_7 = bisect.bisect_left(self.days, self.days[i] + 7)
        result = min(result, self.costs[1] + self.dfs(index_7))
        index_30 = bisect.bisect_left(self.days, self.days[i] + 30)
        result = min(result, self.costs[2] + self.dfs(index_30))
        return result
        
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days, self.n, self.costs = days, len(days), costs
        return self.dfs(0)
# @lc code=end

