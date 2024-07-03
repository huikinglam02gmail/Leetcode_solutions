#
# @lc app=leetcode id=1509 lang=python3
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    choose three numbers out of six max and mins to kill
    combination:
    1. 3 max
    2. 2 max + 1 min
    3. 1 max + 2 min
    4. 3 min    
    '''
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3: return 0
        else:
            min_list = heapq.nsmallest(4, nums)
            max_list = heapq.nlargest(4, nums)
            result = float('inf')
            for i in range(4): result = min(result, max_list[3-i] - min_list[i])
            return result
            # @lc code=end

