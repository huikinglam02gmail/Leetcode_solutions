#
# @lc app=leetcode id=2554 lang=python3
#
# [2554] Maximum Number of Integers to Choose From a Range I
#

# @lc code=start
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        S = 0
        for i in range(1, n + 1):
            if i not in banned:
                if S + i > maxSum: return count
                else:
                    count += 1
                    S += i
        return count

# @lc code=end

