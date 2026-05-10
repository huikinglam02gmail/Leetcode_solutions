#
# @lc app=leetcode id=3912 lang=python3
#
# [3912] Valid Elements in an Array
#

# @lc code=start
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        cur = 0
        use = set()
        for i, num in enumerate(nums):
            if num > cur: use.add(i)
            cur = max(cur, num)
        
        n = len(nums)
        cur = 0
        for i, num in enumerate(nums[::-1]):
            if num > cur: use.add(n - 1 - i)
            cur = max(cur, num)
        return [nums[i] for i in sorted(use)]
# @lc code=end

