#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import random
from typing import List


class Solution:
    '''
    QuickSelect algorithm
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left, mid, right = [], [], []
        for x in nums:
            if x > pivot:
                left.append(x)
            elif x == pivot:
                mid.append(x)
            else:
                right.append(x)        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
# @lc code=end

