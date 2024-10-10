#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
from typing import List


class Solution:
    '''
    2 <= nums.length <= 5 * 10^4: expect O(n) or O(nlogn) solution
    This "width ramp" is to find the earliest elements that is smaller or equal to itself.
    Therefore we should keep a monotonically decreasing stack of the elements, together with their indices
    Rationale:
    nums = [7,9,8,1,0,1,9]
    When we arrived at the second 9, we know the answer is 7 by inspection
    The 9, 8 after it is irrelevant to get the answer
    To search for the index, the bisect module only works for increasingly sorted list. So I just write the binary search function myself
    '''

    def binary_search(self, arr, num):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] > num:
                left = mid + 1
            else:
                right = mid
        return left
    
    def maxWidthRamp(self, nums: List[int]) -> int:
        result, stack = 0, []
        for i, num in enumerate(nums):
            if not stack or num < stack[-1][0]:
                stack.append([num, i])
            else:
                result = max(result, i - stack[self.binary_search(stack, num)][1])
        return result
        
# @lc code=end

