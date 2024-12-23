#
# @lc app=leetcode id=3396 lang=python3
#
# [3396] Minimum Number of Operations to Make Elements in Array Distinct
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numsReversed = []
        appear = {}
        while nums:
            num = nums.pop()
            appear[num] = appear.get(num, 0) + 1
            numsReversed.append(num)
        result = 0
        while len(appear) < len(numsReversed):
            for i in range(min(3, len(numsReversed))):
                num = numsReversed.pop()
                appear[num] -= 1
                if appear[num] == 0: appear.pop(num)
            result += 1
        return result
# @lc code=end

