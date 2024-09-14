#
# @lc app=leetcode id=2155 lang=python3
#
# [2155] All Divisions With the Highest Score of a Binary Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    prefix Sum:
    0 <= i <= n
    number of 0 on left of i (exclusive) = i - prefix[i]
    number of 1 on right of i (inclusive) = prefix[-1] - prefix[i]
    '''
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefix = [0]
        n = len(nums)
        result = []
        maxSoFar = 0
        for num in nums: prefix.append(prefix[-1] + num)
        for i in range(n + 1):
            current =  i + prefix[-1] - 2 * prefix[i]
            if current > maxSoFar:
                while result: result.pop()
                maxSoFar = current
            if current == maxSoFar: result.append(i)
        return result


# @lc code=end

