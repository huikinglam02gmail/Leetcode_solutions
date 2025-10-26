#
# @lc app=leetcode id=3712 lang=python3
#
# [3712] Sum of Elements With Frequency Divisible by K
#

# @lc code=start
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counts = {}
        for num in nums: counts[num] = counts.get(num, 0) + 1
        result = 0
        for k1, v in counts.items():
            if v % k == 0: result += k1 * v 
        return result
# @lc code=end

