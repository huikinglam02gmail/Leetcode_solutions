#
# @lc app=leetcode id=2616 lang=python3
#
# [2616] Minimize the Maximum Difference of Pairs
#

# @lc code=start
from typing import List


class Solution:
    '''
    Firstly, sort nums from small to large
    Then we binary search for the answer. As long as we can get p pair with neighbouring diff < mid, we push left to be mid
    '''
    def canForm(self, p, diff):
        pairs = 0
        i = 0
        while i < len(self.nums) - 1:
            if self.nums[i + 1] - self.nums[i] <= diff:
                pairs += 1
                i += 2
            else:
                i += 1
        return pairs >= p
    
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        self.nums = nums
        l, r = 0, nums[-1] - nums[0]
        while l < r :
            mid = l + (r - l) // 2
            if self.canForm(p, mid):
                r = mid
            else:
                l = mid + 1
        return l
        
# @lc code=end

