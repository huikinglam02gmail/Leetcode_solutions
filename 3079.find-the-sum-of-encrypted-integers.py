#
# @lc app=leetcode id=3079 lang=python3
#
# [3079] Find the Sum of Encrypted Integers
#

# @lc code=start
from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            numSet = set()
            for c in str(num): numSet.add(int(c))
            result += int(str(max(numSet)) * len(str(num)))
        return result
        
# @lc code=end
