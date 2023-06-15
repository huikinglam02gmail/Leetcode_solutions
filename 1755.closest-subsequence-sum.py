#
# @lc app=leetcode id=1755 lang=python3
#
# [1755] Closest Subsequence Sum
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    1 <= nums.length <= 40
    possibility = 2 ^ 40 = 1.0995116e+12;  if list out all the sum and calculate min(sum - goal), will MLE and TLE
    However, we can separate sorted(nums) into 2 parts. We can generate all the possibilities sum in a DP array
    time complexity will be 2* 2^20 = 2097152
    sort both arrays O(2^n * n)
    Then this is a two sum problem: given each sum i in the left, we binary search for the position where goal - i is
    Notice goal - i can be at the end of the array, and we should check for both sides to look for smaller abs(goal - i + j)
    '''

    def dpSumBitMaskSorted(self, nums):
        l = len(nums)
        result = [0]
        for i in range(l):
            for j in range(pow(2, i), pow(2, i + 1)):
                result.append(nums[i] + result[j - pow(2, i)])
        return sorted(result)

    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        if n == 1:
            return min(abs(nums[0] - goal), abs(goal))
        else:
            left, right = nums[:n//2], nums[n//2:]
            leftSumSorted = self.dpSumBitMaskSorted(left)
            rightSumSorted = self.dpSumBitMaskSorted(right)
            nr = len(rightSumSorted)
            result = float("inf")
            for i in leftSumSorted:
                ind = bisect.bisect_left(rightSumSorted, goal - i)
                if 0 <= ind - 1 < nr:
                    result = min(result, abs(rightSumSorted[ind - 1] + i - goal))
                if 0 <= ind < nr:
                    result = min(result, abs(rightSumSorted[ind] + i - goal))
                if 0 <= ind + 1 < nr:
                    result = min(result, abs(rightSumSorted[ind + 1] + i - goal))                    
            return result
# @lc code=end
