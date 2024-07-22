#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        indices = sorted([[i, height] for i, height in enumerate(heights)], key = lambda x: -x[1])
        result = []
        for i in indices: result.append(names[i[0]])
        return result
# @lc code=end

