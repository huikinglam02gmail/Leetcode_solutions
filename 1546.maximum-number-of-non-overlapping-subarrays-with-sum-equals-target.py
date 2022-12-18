#
# @lc app=leetcode id=1546 lang=python3
#
# [1546] Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
#

# @lc code=start
from typing import List


class Solution:
    # We go through nums from left to right
    # Also, we keep track of the number of qualifying subarrays up to each index
    # In the process we keep recording the prefix sum seen and ask if prefix - target was seen before
    # if so, we compare the left element's subarray count vs 1 + subarray count at the index corresponding to the prefix sum - target
    # Also, we update prefix sum: index pair 
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        hashTable = {}
        prefix = 0
        hashTable[prefix] = -1
        n = len(nums)
        counts = [0]*n
        for i, num in enumerate(nums):
            prefix += num
            if i > 0:
                counts[i] = counts[i-1]
            if prefix - target in hashTable:
                lastInd = hashTable[prefix - target]
                counts[i] = max(counts[i], counts[lastInd] + 1)
            hashTable[prefix] = i
        return counts[-1]
# @lc code=end

