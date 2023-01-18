#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from typing import List


class Solution:
    # Use Kadane's algorithm, but slightly more advanced
    # If the max sum subarray does not involve the circular aspect of the array, we can use Kadane's result
    # On the other hand, if the max sum subarray actually span across the boundary
    # the max sum subarray sum = total sum - sum(nums[prefix:suffix])
    # the second term actually correspond to the minimum sum subarray
    # because total (constant) = max sum subarray sum + min sum subarray sum
    # Therefore we can also use Kadane's algorithm to calculate min sum subarray in O(1) space
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, min_sum, max_so_far, min_so_far, total = 0, 0, - float('inf'), float('inf'), 0
        for num in nums:
            max_sum, min_sum = max(max_sum + num, num), min(min_sum + num, num)
            max_so_far, min_so_far = max(max_so_far, max_sum), min(min_so_far, min_sum)
            total += num
            #print(num, max_sum, min_sum, max_so_far, min_so_far)
        if max_so_far > 0:
            return max(max_so_far, total - min_so_far)
        else:
            return max_so_far

# @lc code=end

