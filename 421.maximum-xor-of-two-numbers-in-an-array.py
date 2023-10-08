#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    As LC made testcase to TLE all the python Trie solutions, we resort to something else. A simpler way to do it is to consider the different bits. Going from large to small, we <<= 1 each level and ask if ans + 1 exist in the set of prefixes.
    '''
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0
        numberOfLevels = max(nums).bit_length()
        for i in range(numberOfLevels - 1, -1, -1):
            prefixes = set([num >> i for num in nums])
            result <<= 1
            for prefix in prefixes:
                if (result + 1) ^ prefix in prefixes:
                    result += 1
                    break
        return result
# @lc code=end

