#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= nums.length <= 16
    So use bitMask to represent the subsets.
    Then go through the array to 
    '''
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        subSetMask = [0] * (1 << n)
        i = 0
        hashTable = {}
        for mask in range(1, 1 << n, 1):
            while mask >= (1 << i): i += 1
            subSetMask[mask] = nums[i - 1] | subSetMask[mask - (1 << (i - 1))]
            hashTable[subSetMask[mask]] = hashTable.get(subSetMask[mask], 0) + 1
        return hashTable[max(hashTable.keys())]
# @lc code=end

