#
# @lc app=leetcode id=1793 lang=python3
#
# [1793] Maximum Score of a Good Subarray
#

# @lc code=start
from typing import List


class Solution:
    '''
    The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.
    So a good subarray must include nums[k]. Therefore we start with nums[k] and expand left and right to look for all the possible answer. supposed we have considered nums[i:j + 1]. If nums[i - 1] < nums[j + 1], then we next increment j because there is a possibility nums[i - 1] < min(num[i: j + 1]).
    '''
    def maximumScore(self, nums: List[int], k: int) -> int:
        result = nums[k]
        minSoFar = nums[k]
        i = k
        j = k
        n = len(nums)
        while i >= 0 and j <= n - 1:
            minSoFar = min(minSoFar, nums[i])
            minSoFar = min(minSoFar, nums[j])
            result = max(result, minSoFar * (j - i + 1))
            if i == 0:
                j += 1
            elif j == n - 1:
                i -= 1
            elif nums[i - 1] < nums[j + 1]:
                j += 1
            else:
                i -= 1
        return result           
# @lc code=end
