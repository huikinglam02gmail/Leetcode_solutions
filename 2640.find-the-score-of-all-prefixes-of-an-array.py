#
# @lc app=leetcode id=2640 lang=python3
#
# [2640] Find the Score of All Prefixes of an Array
#

# @lc code=start
from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        last = 0
        maxSoFar = 0
        result = []
        for num in nums:
            maxSoFar = max(maxSoFar, num)
            result.append(last + num + maxSoFar)
            last += num + maxSoFar
        return result
# @lc code=end

