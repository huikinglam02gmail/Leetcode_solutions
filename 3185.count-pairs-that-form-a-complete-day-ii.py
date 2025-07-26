#
# @lc app=leetcode id=3185 lang=python3
#
# [3185] Count Pairs That Form a Complete Day II
#

# @lc code=start
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        modCount = [0] * 24
        for hour in hours: modCount[hour % 24] += 1
        count = 0
        for i in range(24):
            if i % 12 == 0: count += modCount[i] * (modCount[i] - 1)
            else:
                count += modCount[i] * modCount[24 - i]
        return count // 2
    
# @lc code=end

