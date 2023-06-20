#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
from typing import List


class Solution:
    '''
    first initiate result = [-1] * n
    the modification starts from k and ends at n - k - 1. Start a window of size 2 * k  + 1 and add and minus elements when sliding right
    '''
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        if n >= 2 * k + 1:
            windowSum = sum(nums[: 2 * k + 1])
            i = k
            while i <= n - k - 1:
                result[i] = windowSum // (2 * k + 1)
                windowSum -= nums[i - k]
                if i + k + 1 < n:
                    windowSum += nums[i + k + 1] 
                i += 1
        return result

# @lc code=end

