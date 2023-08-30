#
# @lc app=leetcode id=2366 lang=python3
#
# [2366] Minimum Replacements to Sort the Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    Think about the following case:
    nums = [3, 10, 3]
    We should use the last element as the max in the final array, and divide elements before it
    The number of splits we would divide a into will be ceilDiv(a, b) - 1 splits into ceilDiv(a, b) parts
    For example, for a = 10, b = 3, we will divide 10 into [2, 2, 3, 3] 
    = ceilDiv(10, 3) - 1 times.
    And we are interested in the remainder to propagate into the next division to the left. It is nums[i] // ceilDiv(nums[i], remainder)
    '''
    def ceilDiv(self, i, j):
        return - (i // -j)

    def minimumReplacement(self, nums: List[int]) -> int:
        remainder = nums[-1]
        n = len(nums)
        result = 0
        for i in range(n - 2, -1, -1):
            result += self.ceilDiv(nums[i], remainder) - 1
            remainder = nums[i] // self.ceilDiv(nums[i], remainder)
        return result
# @lc code=end

