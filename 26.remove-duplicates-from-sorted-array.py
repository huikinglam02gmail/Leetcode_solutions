#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    # three pointers, one to record last unique value
    # left to record the next element to be swapped
    def removeDuplicates(self, nums: List[int]) -> int:
        left, n = 1, len(nums)
        for right in range(1,n):
            if nums[left-1] < nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return left
         
# @lc code=end

