#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i] % 2 and arr[i + 1] % 2 and arr[i + 2] % 2: return True
        return False
# @lc code=end

