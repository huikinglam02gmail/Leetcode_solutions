#
# @lc app=leetcode id=2951 lang=python3
#
# [2951] Find the Peaks
#

# @lc code=start
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        result = []
        for i in range(1, n - 1, 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]: result.append(i)
        return result
# @lc code=end

