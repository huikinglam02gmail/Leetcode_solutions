#
# @lc app=leetcode id=2171 lang=python3
#
# [2171] Removing Minimum Number of Magic Beans
#

# @lc code=start
from typing import List


class Solution:
    '''
    First sort beans
    Then we test if each final bean Count gives the minimum beans to remove
    To help with sum, we prepare prefix sum as well
    cost to set final level at beans[i] = prefix[i] + prefix[-1] - prefix[i + 1] - (n - 1 - i) * beans[i] 
    '''
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        prefix = [0]
        n = len(beans)
        for bean in beans: prefix.append(prefix[-1] + bean)
        result = float("inf")
        for i in range(n): result = min(result, prefix[i] + prefix[-1] - prefix[i + 1] - (n - 1 - i) * beans[i])
        return result


            
# @lc code=end

