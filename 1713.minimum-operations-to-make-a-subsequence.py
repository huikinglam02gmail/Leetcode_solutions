#
# @lc app=leetcode id=1713 lang=python3
#
# [1713] Minimum Operations to Make a Subsequence
#

# @lc code=start
import bisect
from typing import List


class Solution:

    '''
    The problem is asking for longest common subsequence between two arrays with a twist: we want to get the longest footprint of target on arr.
    Because we know target contains no duplicates, we can record the index of each number in target in a dictionary
    Then we go to arr. If num is not inside the dictionary, we can skip. If not, we construct the index array of which num appear in target
    Finally the problem becomes: find the longest increasing subsequence of the resultant index array. That we already did before in Leetcode 300. The answer is len(target) - LISlength
    '''

    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []
        for i, num in enumerate(nums):
            if i == 0 or num > result[-1]: 
                result.append(num)
            elif num < result[-1]:
                index = bisect.bisect_left(result, num)
                result[index] = num
        return len(result)

    def minOperations(self, target: List[int], arr: List[int]) -> int:
        hashTable = {}
        for i, num in enumerate(target):
            hashTable[num] = i
        result = []
        for num in arr:
            if num in hashTable:
                result.append(hashTable[num])
        return len(target) - self.lengthOfLIS(result)
# @lc code=end

