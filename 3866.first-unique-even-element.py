#
# @lc app=leetcode id=3866 lang=python3
#
# [3866] First Unique Even Element
#

# @lc code=start
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        seen = {}
        for num in nums:
            if num % 2 == 0:
                seen[num] = seen.get(num, 0) + 1
        for num in nums:
            if seen.get(num, 0) == 1:
                return num
        return -1

# @lc code=end

