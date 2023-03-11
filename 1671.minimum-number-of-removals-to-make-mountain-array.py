#
# @lc app=leetcode id=1671 lang=python3
#
# [1671] Minimum Number of Removals to Make Mountain Array
#

# @lc code=start
import bisect
from operator import itemgetter
from typing import List


class Solution:
    '''
    minimum removal to make mountain array = n - len(LIS from left) - len(LIS from right) + 1
    For  0 < i < n - 1, find length of LIS ending at nums[i]. To do that, we record these in dpForward[i] and dpReverse[i].
    '''

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        forward = []
        reverse = []
        dpForward = [0]*(n + 2)
        dpReverse = [0]*(n + 2)
        forward.append([0, 0])
        for i in range(n):
            index = bisect.bisect_left(forward, nums[i], key = itemgetter(0))
            if index == len(forward):
                dpForward[i + 1] = len(forward)
                forward.append([nums[i], i + 1])
            else:
                dpForward[i + 1] = dpForward[forward[index - 1][1]] + 1
                if forward[index][0] > nums[i]:
                    forward[index] = [nums[i], i + 1] 
        
        reverse.append([0, n + 1])
        for i in range(n - 1, -1, -1):
            index = bisect.bisect_left(reverse, nums[i], key = itemgetter(0))
            if index == len(reverse):
                dpReverse[i + 1] = len(reverse)
                reverse.append([nums[i], i + 1])
            else:
                dpReverse[i + 1] = dpReverse[reverse[index - 1][1]] + 1
                if reverse[index][0] > nums[i]:
                    reverse[index] = [nums[i], i + 1]

        result = n
        for i in range(2, n):
            if dpForward[i] > 1 and dpReverse[i] > 1:
                result = min(result, n + 1 - dpForward[i] - dpReverse[i])
        return result

        
# @lc code=end
