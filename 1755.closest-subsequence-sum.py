#
# @lc app=leetcode id=1755 lang=python3
#
# [1755] Closest Subsequence Sum
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= nums.length <= 40
    possibility = 2 ^ 40 = 1.0995116e+12;  if list out all the sum and calculate min(sum - goal), will MLE and TLE
    However, we can separate sorted(nums) into 2 parts. We can generate all the possibilities sum in a DP array
    time complexity will be 2* 2^20 = 2097152
    sort both arrays O(2^n * n)
    Then we can do two sum closest to target for each sum in left array O(n * 2^n)
    '''
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        if n == 1:
            return abs(nums[0] - goal)
        else:
            left, right = nums[:n//2], nums[n//2:]
# @lc code=end

