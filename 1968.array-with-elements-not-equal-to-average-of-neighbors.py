#
# @lc app=leetcode id=1968 lang=python3
#
# [1968] Array With Elements Not Equal to Average of Neighbors
#

# @lc code=start
from typing import List


class Solution:
    '''
    We can sort nums first
    Then put the large ones on odd and small ones on even indices
    '''
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        result = [0] * n
        for i in range(0, n, 2):
            result[i] = nums[n - 1 - i // 2]
        for i in range(1, n, 2):
            result[i] = nums[i // 2]
        return result
# @lc code=end

