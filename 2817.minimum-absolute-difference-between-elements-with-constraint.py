#
# @lc app=leetcode id=2817 lang=python3
#
# [2817] Minimum Absolute Difference Between Elements With Constraint
#

# @lc code=start
from typing import List

from sortedcontainers import SortedList


class Solution:
    '''
    We can use a sorted list to maintain the elements that are at least x distance away from the current element.
    For each element nums[i], we add nums[i - x] to the sorted list (if i >= x).
    Then we use binary search to find the closest element to nums[i] in the sorted list and update the minimum absolute difference.
    '''
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        min_diff = float('inf')
        sl = SortedList()
        for i, num in enumerate(nums):
            if i >= x:
                sl.add(nums[i - x])
            if sl:
                pos = sl.bisect_left(num)
                if pos < len(sl): min_diff = min(min_diff, abs(num - sl[pos]))
                if pos > 0: min_diff = min_diff = min(min_diff, abs(num - sl[pos - 1]))
        return min_diff
# @lc code=end

