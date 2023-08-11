#
# @lc app=leetcode id=1846 lang=python3
#
# [1846] Maximum Element After Decreasing and Rearranging
#

# @lc code=start
from typing import List


class Solution:
    '''
    Notice we can only decrease, not increase.
    So first we sort arr
    Then going from left to right, the number that we put in is min(pre + 1, a)
    '''
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        pre = 0
        for a in arr:
            pre = min(pre + 1, a)
        return pre
# @lc code=end

