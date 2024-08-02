#
# @lc app=leetcode id=2134 lang=python3
#
# [2134] Minimum Swaps to Group All 1's Together II
#

# @lc code=start
from typing import List


class Solution:
    '''
    To get rid of circular array, append nums to nums
    Then count total number of 1 = total
    Then use prefix sum to get the min(total - sum)
    '''
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total = nums.count(1)
        nums = nums + nums
        prefix = [0]
        result = total
        for num in nums: prefix.append(prefix[-1] + num)
        for i in range(total, n + total + 1, 1): result = min(result, total - prefix[i] + prefix[i - total])
        return result
        
# @lc code=end

