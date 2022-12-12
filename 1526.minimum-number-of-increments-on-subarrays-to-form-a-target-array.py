#
# @lc app=leetcode id=1526 lang=python3
#
# [1526] Minimum Number of Increments on Subarrays to Form a Target Array
#

# @lc code=start


from typing import List


class Solution:
    # No need to find complicated range minimum and maximum
    # Between consecutive elements, we just need to notice whether the second element is larger than that of the first
    # If so, we need an extra step to stack up diff layers
    def minNumberOperations(self, target: List[int]) -> int:
        prev, n, result = 0, len(target), 0
        for i in range(n):
            result += max(target[i] - prev, 0)
            prev = target[i]
        return result
# @lc code=end

