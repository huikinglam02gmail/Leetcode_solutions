#
# @lc app=leetcode id=2568 lang=python3
#
# [2568] Minimum Impossible OR
#

# @lc code=start
from typing import List


class Solution:
    '''
    ORing different nums always increase the final OR. So the answer must be one of 1 << i, in which if 1 << i is not in nums, that's the answer
    '''
    def minImpossibleOR(self, nums: List[int]) -> int:
        numsSet = set(nums)
        for i in range(32):
            if 1 << i not in numsSet: return 1 << i
        return -1
        
# @lc code=end

