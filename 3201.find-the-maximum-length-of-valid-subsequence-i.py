#
# @lc app=leetcode id=3201 lang=python3
#
# [3201] Find the Maximum Length of Valid Subsequence I
#

# @lc code=start
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        length = [0] * 4
        for num in nums:
            newLength = [0] * 4
            if num % 2 == 0:
                newLength[0] = length[0] + 1
                newLength[2] = length[3] + 1
            else:
                newLength[1] = length[1] + 1
                newLength[3] = length[2] + 1
            for i in range(4): length[i] = max(newLength[i], length[i])
        return max(length)
            
# @lc code=end

