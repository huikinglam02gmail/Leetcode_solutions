#
# @lc app=leetcode id=2866 lang=python3
#
# [2866] Beautiful Towers II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Try every index as the peak of the tower, and calculate the maximum sum of heights with that peak.
    Use a monotonic stack to efficiently compute the left and right contributions.
    '''
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        left = self.beautifulTowersPrefixSum(maxHeights)
        right = self.beautifulTowersPrefixSum(maxHeights[::-1])[::-1]
        result = 0
        for i in range(len(maxHeights)):
            result = max(result, left[i] + right[i] - maxHeights[i])
        return result
    
    def beautifulTowersPrefixSum(self, maxHeights: List[int]) -> int:
        left = []
        stack = [-1]
        prefixSum = 0
        for i in range(len(maxHeights)):
            while stack[-1] >= 0 and maxHeights[stack[-1]] >= maxHeights[i]:
                j = stack.pop()
                prefixSum -= maxHeights[j] * (j - stack[-1])
            prefixSum += maxHeights[i] * (i - stack[-1])
            stack.append(i)
            left.append(prefixSum)
        return left
        
# @lc code=end

