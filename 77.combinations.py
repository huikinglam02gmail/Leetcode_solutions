#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [i for i in range(1,n+1)]
        return list(combinations(numbers, k))
# @lc code=end

