#
# @lc app=leetcode id=3375 lang=python3
#
# [3375] Minimum Operations to Make Array Values Equal to K
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        allKeys = sorted(set(nums))
        if len(allKeys) == 1 and allKeys[0] == k: return 0
        elif k >= allKeys[-1] or k > allKeys[0]: return -1
        elif k < allKeys[0]: return len(allKeys)
        else: return len(allKeys) - 1
# @lc code=end

