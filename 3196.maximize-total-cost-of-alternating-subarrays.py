#
# @lc app=leetcode id=3196 lang=python3
#
# [3196] Maximize Total Cost of Alternating Subarrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    When we group neighboring elements, we can essentially choosing whether to flip the sign of each element or not.
    For example, for the array [a, b, c], we can have:
    - No flips: +a +b +c = [a, b] + [c]
    - Flip b: +a -b +c = [a, -b, c]
    - Flip c: +a +b -c = [a] + [b, c]
    dp[i][0] = max total cost ending at index i with the ith element not flipped
    dp[i][1] = max total cost ending at index i with the ith element flipped
    Take note: the first element cannot be flipped
    '''

    def maximumTotalCost(self, nums: List[int]) -> int:
        dp = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            dp[0], dp[1] = nums[i] + max(dp[0], dp[1]), -nums[i] + dp[0]
        return max(dp)

# @lc code=end

