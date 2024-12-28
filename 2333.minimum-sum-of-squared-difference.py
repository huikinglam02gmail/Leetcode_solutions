#
# @lc app=leetcode id=2333 lang=python3
#
# [2333] Minimum Sum of Squared Difference
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    k1 and k2 can be simplified to k = k1 + k2
    (a + 1) ^ 2 + (a - 1) ^ 2 = 2 * a ^ 2 + 2 > a ^ 2
    we binary search for the minimum of maximum diffs in the final diff array, such that the number of steps needed <= k
    There would be extras which would use l - 1 instead of l.
    '''
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        self.diffs = [abs(num1 - num2) for num1, num2 in zip(nums1, nums2)]
        l, r = 0, max(self.diffs) + 1
        while l < r:
            mid = l + (r - l) // 2
            numSteps = self.steps(mid)
            if numSteps > k1 + k2: l = mid + 1
            else: 
                r = mid
                extra = k1 + k2 - numSteps
        result = 0
        for diff in self.diffs:
            use = 0
            if diff >= l and extra > 0:
                use += 1
                extra -= 1
            finalDiff = min(diff, max(0, l - use))
            result += finalDiff * finalDiff
        return result
    
    def steps(self, maxDiff):
        result = 0
        for diff in self.diffs: result += max(0, diff - maxDiff)
        return result
            

# @lc code=end
