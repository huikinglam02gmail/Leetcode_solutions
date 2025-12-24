#
# @lc app=leetcode id=2975 lang=python3
#
# [2975] Maximum Square Area by Removing Fences From a Field
#

# @lc code=start
from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences = [1] + sorted(hFences) + [m]
        vFences = [1] + sorted(vFences) + [n]
        allHeights = set()
        for i in range(len(hFences) - 1):
            for j in range(i + 1, len(hFences)):
                allHeights.add(hFences[j] - hFences[i])
        allWidths = set()
        for i in range(len(vFences) - 1):
            for j in range(i + 1, len(vFences)):
                allWidths.add(vFences[j] - vFences[i])
        maxArea = 0
        for height in allHeights:
            if height in allWidths:
                maxArea = max(maxArea, height * height)
        return maxArea % 1000000007 if maxArea > 0 else -1
# @lc code=end

