#
# @lc app=leetcode id=1712 lang=python3
#
# [1712] Ways to Split Array Into Three Subarrays
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    When we split the array into 3 parts, there are 2 barriers
    Once we fix the left wall, we impose the condition to the right wall: sum(nums[left + 1:right + 1]) <= sum(nums[left + 1:]) // 2
    Use prefix sum to get the subarray sums in O(1) time
    To ensure for nonempty subarray, right wall is at least left + 1 and no larger than n
    '''
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        n = len(nums)
        prefix = [0]
        result = 0
        for num in nums:
            prefix.append(prefix[-1] + num)
        leftRightMost = min(bisect.bisect_right(prefix, prefix[-1] // 3), n - 1)
        for left in range(1, leftRightMost):
            rightLeftMost = max(left + 1, bisect.bisect_left(prefix, 2*prefix[left]))
            rightRightMost = min(n, bisect.bisect_right(prefix, (prefix[-1] + prefix[left]) // 2))
            result += max(0, rightRightMost - rightLeftMost)
            if result > MOD:
                result %= MOD
        return result
# @lc code=end
