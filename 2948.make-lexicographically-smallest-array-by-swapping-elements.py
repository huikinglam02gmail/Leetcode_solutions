#
# @lc app=leetcode id=2948 lang=python3
#
# [2948] Make Lexicographically Smallest Array by Swapping Elements
#

# @lc code=start
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        data = [[num, i] for i, num in enumerate(nums)]
        data.sort()
        groups = []
        last = - float("inf")
        for num, i in data:
            if num - last > limit: groups.append([])
            groups[-1].append([num, i])
            last = num
        result = [-1] * len(nums)
        for group in groups:
            indiceSorted = sorted([x[1] for x in group])
            for j in range(len(indiceSorted)): result[indiceSorted[j]] = group[j][0]
        return result
# @lc code=end

