#
# @lc app=leetcode id=1589 lang=python3
#
# [1589] Maximum Sum Obtained of Any Permutation
#

# @lc code=start
from typing import List


class Solution:
    # First go through requests to record how many times each index is called
    # Then fill nums from large to small frequency
    # Then use prefix sum array to calculate the result
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        intervals, arr = [], []
        appearance, n, ind, result, MOD = 0, len(nums), 0, 0, pow(10,9) + 7
        for start, end in requests:
            intervals.append([start, 1])
            intervals.append([end + 1, -1])
        intervals.sort()
        for i in range(n):
            while ind < len(intervals) and intervals[ind][0] == i:
                appearance += intervals[ind][1]
                ind += 1
            arr.append([appearance, i])
        arr.sort(key = lambda x: - x[0])
        nums.sort(key = lambda x: - x)
        numNew = [0]*n
        for i in range(n):
            numNew[arr[i][1]] = nums[i]
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + numNew[i])
        for start, end in requests:
            result += prefix[end + 1] - prefix[start]
        return result % MOD

        
# @lc code=end
