#
# @lc app=leetcode id=3880 lang=python3
#
# [3880] Minimum Absolute Difference Between Two Values
#

# @lc code=start
import bisect


class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        ones = []
        twos = []
        for i, num in enumerate(nums):
            if num == 1:
                ones.append(i)
            elif num == 2:
                twos.append(i)
        if not ones or not twos:
            return -1
        result = float('inf')
        for i in ones:
            j = bisect.bisect_left(twos, i)
            if 0 <= j + 1 < len(twos):
                result = min(result, abs(i - twos[j + 1]))
            if 0 <= j < len(twos):
                result = min(result, abs(i - twos[j]))
            if 0 <= j - 1 < len(twos):
                result = min(result, abs(i - twos[j - 1]))
        return result
# @lc code=end
