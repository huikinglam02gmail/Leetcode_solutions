#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#

# @lc code=start
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff, n = arr[1] - arr[0], len(arr)
        for i in range(1,n-1):
            if arr[i] + diff != arr[i+1]:
                return False
        return True
# @lc code=end

