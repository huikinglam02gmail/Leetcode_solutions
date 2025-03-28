#
# @lc app=leetcode id=2588 lang=python3
#
# [2588] Count the Number of Beautiful Subarrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    record prefix XOR
    '''
    def beautifulSubarrays(self, nums: List[int]) -> int:
        prefixXOR = {}
        prefixXOR[0] = 1
        S = 0
        result = 0
        for num in nums:
            S ^= num
            result += prefixXOR.get(S, 0)
            prefixXOR[S] = prefixXOR.get(S, 0) + 1
        return result
# @lc code=end

